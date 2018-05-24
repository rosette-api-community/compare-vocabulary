#!/usr/bin/env python3

"""Compare vocabularies from directories of text files"""

import csv
import fnmatch
import json
import os
import re
import sys

from collections import Counter, namedtuple
from getpass import getpass
from itertools import chain, zip_longest
from operator import methodcaller, itemgetter
from rosette.api import API, DocumentParameters, RosetteException

DEFAULT_ROSETTE_API_URL = 'https://api.rosette.com/rest/v1/'
STOPWORDS_FILE = os.path.join(os.path.dirname(__file__), 'stopwords.json')
# This namedtuple is just a convenient data reprsentation for vocabulary terms
Lemma = namedtuple('Lemma', ['lemma', 'pos'])

def load_stopwords(filename):
    """Load stopwords lists from JSON file"""
    with open(filename, mode='r') as f:
        return  json.loads(f.read())

def find_files(directory='.', pattern='*', recursive=True):
    """Find files in the current directory that match the given pattern"""
    pattern = re.compile(fnmatch.translate(pattern))
    walk = os.walk(directory, followlinks=True)
    if recursive:
        return (os.path.realpath(os.path.join(directory, filename))
            for directory, subdirectories, filenames in walk
            for filename in filenames if re.match(pattern, filename))
    else:
        return (os.path.realpath(os.path.join(directory, filename))
            for filename in os.listdir(directory)
            if re.match(pattern, filename))

def request(content, endpoint, api, language=None, uri=False, **kwargs):
    """Request Rosette API results for the given content and endpoint.

    This method gets the requested results from the Rosette API as JSON.  If
    api's output parameter has been set to "rosette" then the JSON will consist
    of an A(nnotated) D(ata) M(odel) or ADM.  An ADM is a Python dict
    representing document content, annotations of the document content,
    and document metadata.
    
    content:  path or URI of a document for the Rosette API to process
    endpoint: a Rosette API endpoint string (e.g., 'entities')
              (see https://developer.rosette.com/features-and-functions)
    api:      a rosette.api.API instance
              (e.g., API(user_key=<key>, service_url=<url>))
    language: an optional ISO 639-2 T language code
              (the Rosette API will automatically detect the language of the
              content by default)
    uri:      specify that the content is to be treated as a URI and the
              the document content is to be extracted from the URI
    kwargs:   additional keyword arguments
              (e.g., if endpoint is 'morphology' you can specify facet='lemmas';
              see https://developer.rosette.com/features-and-functions for
              complete documentation)
    """
    parameters = DocumentParameters()
    if uri:
        parameters['contentUri'] = content
    else:
        parameters['content'] = content
    parameters['language'] = language
    try:
        adm = methodcaller(endpoint, parameters, **kwargs)(api)
        return adm
    except RosetteException as e:
        print(f'[{e.status}]: {e.message}', file=sys.stderr)

def load(filename):
    """Load text from a file"""
    with open(filename, mode='r') as f:
        return f.read()

def lemmas(directory, api):
    """Generate lemma/POS annotations (i.e., Lemma namedtuples) via Rosette API
    analysis for a directory of text files
    
    directory : a directory of text files
          api : a rosette.api.API instance
    """
    for filename in find_files(directory, pattern='*.txt'):
        adm = request(load(filename), 'morphology', api)
        if adm is not None:
            for lemma in adm['attributes']['token']['items']:
                first, *rest = lemma['analyses']
                yield Lemma(first['lemma'], first['partOfSpeech'])

def fdist(directory, api, n, stopwords):
    """Get the top n most frequent lemmas as a lemma/POS:frequency distribution 
    for the vocabulary of the text in a directory
    
    directory : a directory of text files
          api : a rosette.api.API instance
            n : an integer specifying that the frequency distribution includes 
                ony the top n most frequent terms (if n is None all vocabulary 
                terms are included)"""
    return dict(
        Counter((
            term for term in lemmas(directory, api)
            if term.lemma.lower() not in set(stopwords or [])
        )).most_common(n)
    )

def compare_all(*fds):
    """A comparator that includes the union of the vocabularies from the given
    frequency distributions
    
    fds : a collection of frequency distribution dicts
          (dicts map Lemma -> int; see fdist())
    """
    fill = (Lemma('', ''), '')
    fds = (sorted(fd.items(), key=itemgetter(1), reverse=True) for fd in fds)
    for terms_freqs in zip_longest(*fds, fillvalue=fill):
        yield chain(
            *((term.lemma, term.pos, freq or '') for term, freq in terms_freqs)
        )

def compare_intersection(*fds):
    """A comparator that includes only the intersection of the vocabularies
    from the given frequency distributions
    
    fds : a collection of frequency distributions
          (dicts mapping Lemma -> int; see fdist())
    """
    # Restrict the vocabulary to the intersection of all frequency distributions
    vocabulary = sorted(
        set.intersection(*(set(fd) for fd in fds)),
        key=lambda term: tuple(fd.get(term) for fd in fds),
        reverse=True
    )
    for term in vocabulary:
        yield chain(*((term.lemma, term.pos, fd[term]) for fd in fds))

def compare_disjunction(*fds):
    """A comparator that includes only the disjunction of the vocabularies
    from the given frequency distributions
    
    fds: a collection of frequency distributions
        (dicts mapping Lemma -> int; see fdist())
    """
    # Restrict the vocabulary to those terms that occur in each fd individually,
    # but do not occur in the intersection of all fds
    intersection = set.intersection(*(set(fd) for fd in fds))
    yield from compare_all(*(
        {term: fd[term] for term in set(fd).difference(intersection)}
        for fd in fds
    ))

def compare_unique(*fds):
    """A comparator that includes only terms that are unique to a particular
    corpus
    
    fds: a collection of frequency distributions
        (dicts mapping Lemma -> int; see fdist())
    """
    indices = range(len(fds))
    for i, fd in enumerate(fds):
        rest_vocabulary = set.union(*(
            set(fds[j]) for j in indices if j != i
        ))
        for term in set(fd):
            if term in rest_vocabulary:
                fd.pop(term)
    yield from compare_all(*(fds))

COMPARISONS = {
    'all': compare_all,
    'intersection': compare_intersection,
    'disjunction': compare_disjunction,
    'unique': compare_unique
}

def main(directories, api, comparison, n, stopwords):
    """Create frequency distributions from the vocabularies of each directory
    and write out a tabular representatin to stdout
    
    directories : a list of directories of text files
            api : a rosette.api.API instance
     comparsion : a comparator function (see COMPARISONS)
              n : an integer specifying that the frequency distribution includes
                  ony the top n most frequent terms (if n is None all vocabulary
                  terms are included)"""
    fds = [fdist(directory, api, n, stopwords) for directory in directories]
    writer = csv.writer(sys.stdout, delimiter='\t')
    header = chain(
        *((f'{d}:lemma', f'{d}:pos', f'{d}:frequency') for d in directories)
    )
    writer.writerow(header)
    writer.writerows(comparison(*fds))

if __name__ == '__main__':
    stopwords = load_stopwords(STOPWORDS_FILE)
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        'directories',
        nargs='+',
        help='a list of directories of text files'
    )
    parser.add_argument(
        '-c', '--comparison',
        choices=sorted(COMPARISONS),
        default='all',
        help=(
            'all: include the union of all terms across all corpora; '
            'intersection: include only those terms that occur in all corpora; '
            'disjunction: include only those terms that occur in some of the '
            'corpora, but not in all of the corpora; '
            'unique: include only those terms that are unique to each corpus'
        )
    )
    parser.add_argument(
        '-n', '--top-n',
        type=int,
        default=None,
        help='how many lexical items to compare'
    )
    parser.add_argument(
        '-l', '--language',
        default=None,
        choices=sorted(stopwords.keys()),
        help=(
            'ISO 639-2/T three-letter language code (this indicates which '
            'stopword list to use)'
        )
    )
    parser.add_argument(
        '-k', '--key',
        help='Rosette API Key',
        default=None
    )
    parser.add_argument(
        '-a', '--api-url',
        help='Alternative Rosette API URL',
        default=DEFAULT_ROSETTE_API_URL
    )
    args = parser.parse_args()
    # Get the user's Rosette API key
    key = (
        os.environ.get('ROSETTE_USER_KEY') or
        args.key or
        getpass(prompt='Enter your Rosette API key: ')
    )
    # Instantiate the Rosette API
    api = API(user_key=key, service_url=args.api_url)
    api.set_url_parameter('output', 'rosette')
    comparator = COMPARISONS[args.comparison]
    main(
        args.directories,
        api,
        comparator,
        args.top_n,
        stopwords.get(args.language, [])
    )

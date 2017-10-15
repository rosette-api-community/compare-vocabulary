#!/usr/bin/env python3

"""Visualize term frequency distributions via Rosette API analyses"""

import os

from getpass import getpass
from collections import namedtuple

from bs4 import BeautifulSoup
from compare_vocabulary import fdist, DEFAULT_ROSETTE_API_URL
from rosette.api import API
from scipy.interpolate import interp1d

Pos = namedtuple('Pos', ['short', 'long'])
Color = namedtuple('Color', ['hex', 'name'])

COLOR = {
    Pos('ADJ', 'Adjective'): Color('#4E8975', 'seagreen'),
    Pos('ADP', 'Adposition'): Color('#A52A2A', 'brown'),
    Pos('ADV', 'Adverb'): Color('#00FF00', 'lime'),
    Pos('AUX', 'Auxiliary verb'): Color('#0000FF', 'blue'),
    Pos('CONJ', 'Coordinating conjunction'): Color('#ff4500', 'orangered'),
    Pos('DET', 'Determiner'): Color('#c0c0c0', 'silver'),
    Pos('INTJ', 'Interjection'): Color('#493D26', 'mocha'),
    Pos('NOUN', 'Noun'): Color('#FFA500', 'orange'),
    Pos('NUM', 'Numeral'): Color('#6698FF', 'skyblue'),
    Pos('PART', 'Particle'): Color('#FF00FF', 'magenta'),
    Pos('PRON', 'Pronoun'): Color('#FF0000', 'red'),
    Pos('PROPN', 'Proper noun'): Color('#8D38C9', 'violet'),
    Pos('PUNCT', 'Punctuation'): Color('#008080', 'teal'),
    Pos('SCONJ', 'Subordinating conjunction'): Color('#EDDA74', 'goldenron'),
    Pos('SYM', 'Symbol'): Color('#808000', 'olive'),
    Pos('VERB', 'Verb'): Color('#800080', 'purple'),
    Pos('X', 'Other'): Color('#000000', 'black'),
}

def color_key():
    """Generate a POS:color key as HTML"""
    html = '<h2>Color Key</h2>'
    html += '<ul>'
    html += '\n'.join(
        f'<li><font color="{color.hex}">{pos.short}:{pos.long}</font></li>'
        for pos, color in COLOR.items()
    )
    html += '</ul>'
    return html

def visualize(fd, pos_tags=None):
    """Visualize a frequency distribution (fd) as a word-cloud in HTML"""
    if pos_tags is not None:
        fd = {t: f for t, f in fd.items() if t.pos in pos_tags}
    color = {pos.short: color.hex for pos, color in COLOR.items()}
    frequencies = sorted(fd.values())
    resize = interp1d((min(frequencies), max(frequencies)), (1, 100))
    size = dict(zip(frequencies, resize(frequencies)))
    html = '\n'.join(
        f'''<font
            color="{color[t.pos]}"
            size={size[f]}
            title="{t.lemma}/{t.pos} ({f})"
        >
        {t.lemma}
        </font>''' for t, f in fd.items()
    )
    return html

if __name__ == '__main__':
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
        '-n', '--top-n',
        type=int,
        default=None,
        help='how many lexical items to compare'
    )
    parser.add_argument(
        '-t', '--pos-tags',
        default=None,
        metavar='POS',
        choices=sorted(pos.short for pos in COLOR),
        nargs='+',
        help='a white-list of part-of-speech (POS) tags to include'
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
    api.setUrlParameter('output', 'rosette')
    
    html = color_key()
    
    for directory in args.directories:
        html += f'<h1>{directory}<h1>'
        html += visualize(
            fdist(directory, api, args.top_n),
            pos_tags=args.pos_tags
        )
    
    page = BeautifulSoup(html, 'html5lib')
    print(page.prettify())

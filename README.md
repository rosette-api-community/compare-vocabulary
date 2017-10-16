# compare-vocabulary

This repository includes Python examples that leverage the [`/morphology/lemmas` endpoint of Rosette API](https://developer.rosette.com/features-and-functions#morphological-analysis-lemmas) for:

* Comparing vocabulary terms in different sets of documents
* Visualizing frequency distributions of vocabulary terms and their parts-of-speech

## [Jupyter Notebook]((http://nbviewer.jupyter.org/github/zyocum/compare-vocabulary/blob/master/visualize.ipynb))

The simplest way to get started is to access the Jupyter notebook online [**here**](http://nbviewer.jupyter.org/github/zyocum/compare-vocabulary/blob/master/visualize.ipynb).  You can also run the notebook locally (after following [the setup instructions below](https://github.com/zyocum/compare-vocabulary/blob/master/README.md#setup)) by running:

	(compare-vocabulary) $ jupyter notebook visualize.ipynb

Some corpora of poems by several famous poets are provided as examples in [`data`](https://github.com/zyocum/compare-vocabulary/tree/master/data).  If you'd like to analyze your own data, you can add to/replace those subdirectories with directories of your own plain-text files.

## Setup

This repository is written for Python 3.6.3 or later.  It is recommended that you set up a virtual environment first.  In this directory run:

    $ python3 $(which virtualenv) .

Then activate the environment:

    $ source bin/activate

Then install the dependencies:

    (compare-vocabulary) $ pip3 install -r requirements.txt

Now you should be all set to run the scripts or launch the notebook.

## `compare_vocabulary.py`

This is a Python script with a command-line driver for producing a tabular comparison of lemma/parts-of-speech term frequencies across different corpora.

### Usage

    (compare-vocabulary) $ ./compare_vocabulary.py -h
    usage: compare_vocabulary.py [-h] [-c {all,intersection}] [-n TOP_N] [-k KEY]
                                 [-a API_URL]
                                 directories [directories ...]

    Compare vocabularies from directories of text files

    positional arguments:
      directories           a list of directories of text files

    optional arguments:
      -h, --help            show this help message and exit
      -c {all,intersection}, --comparison {all,intersection}
                            select whether to compare all vocabulary terms (all)
                            or count only the frequencies of terms that occur at
                            least once in each directory (intersection) (default:
                            all)
      -n TOP_N, --top-n TOP_N
                            how many lexical items to compare (default: None)
      -k KEY, --key KEY     Rosette API Key (default: None)
      -a API_URL, --api-url API_URL
                            Alternative Rosette API URL (default:
                            https://api.rosette.com/rest/v1/)

For example, to write out tabular comparison data to file as TSV:

    (compare-vocabulary) $ ./compare_vocabulary.py data/{carroll,shakespeare} -n 50 > carroll_vs_shakespeare.tsv

And to quickly reformat the the TSV file contents in a more human-readable format:

    (compare-vocabulary) $ column -t < carroll_vs_shakespeare.tsv
    data/carroll:lemma  data/carroll:pos  data/carroll:frequency  data/shakespeare:lemma  data/shakespeare:pos  data/shakespeare:frequency
    ,                   PUNCT             110                     ,                       PUNCT                 69
    the                 DET               89                      and                     CONJ                  31
    and                 CONJ              61                      the                     DET                   27
    be                  VERB              52                      I                       PRON                  24
    -                   PUNCT             50                      of                      ADP                   18
    """"                PUNCT             40                      .                       PUNCT                 18
    .                   PUNCT             35                      in                      ADP                   16
    you                 PRON              33                      be                      VERB                  16
    !                   PUNCT             28                      ;                       PUNCT                 14
    `                   PUNCT             27                      thou                    PRON                  12
    '                   PUNCT             26                      's                      PART                  10
    I                   PRON              24                      -                       PUNCT                 10
    he                  PRON              23                      shall                   AUX                   9
    say                 VERB              23                      with                    ADP                   8
    a                   DET               21                      to                      ADP                   8
    to                  PART              20                      :                       PUNCT                 8
    have                VERB              20                      love                    NOUN                  8
    of                  ADP               19                      sonnet                  NOUN                  7
    they                PRON              19                      not                     PART                  7
    it                  PRON              17                      this                    DET                   7
    do                  VERB              15                      more                    ADV                   7
    we                  PRON              15                      he                      DET                   7
    he                  DET               14                      all                     DET                   7
    in                  ADP               14                      to                      PART                  7
    ;                   PUNCT             14                      a                       DET                   7
    :                   PUNCT             12                      by                      ADP                   7
    ?                   PUNCT             11                      which                   PRON                  7
    I                   DET               11                      nor                     CONJ                  6
    to                  ADP               11                      when                    ADV                   6
    all                 DET               11                      eye                     NOUN                  6
    with                ADP               10                      that                    DET                   6
    come                VERB              10                      I                       DET                   6
    but                 SCONJ             9                       have                    VERB                  6
    she                 PRON              9                       it                      PRON                  6
    Walrus              PROPN             9                       but                     SCONJ                 5
    on                  ADP               8                       time                    NOUN                  5
    this                DET               8                       as                      SCONJ                 5
    for                 ADP               7                       if                      SCONJ                 5
    give                VERB              7                       on                      ADP                   5
    so                  ADV               7                       or                      CONJ                  5
    Carpenter           PROPN             7                       you                     PRON                  4
    you                 DET               6                       these                   DET                   4
    very                ADV               6                       death                   NOUN                  4
    youth               NOUN              6                       from                    ADP                   4
    one                 NUM               6                       woe                     NOUN                  4
    as                  ADP               6                       can                     AUX                   4
    not                 PART              6                       long                    ADV                   4
    yet                 ADV               5                       see                     VERB                  4
    at                  ADP               5                       she                     DET                   4
    that                DET               5                       than                    CONJ                  3

## visualize.py

This is a Python script with a command-line driver for producing an HTML visualization of lemma/parts-of-speech term frequencies across different corpora.  In the visualization lemmas are color-coded according to their part-of-speech (POS) tag and their size is scaled relative to their frequency.

    (compare-vocabulary) $ ./visualize.py -h 2>/dev/null
    usage: visualize.py [-h] [-n TOP_N] [-t POS [POS ...]] [-k KEY] [-a API_URL]
                        directories [directories ...]

    Visualize term frequency distributions via Rosette API analyses

    positional arguments:
      directories           a list of directories of text files

    optional arguments:
      -h, --help            show this help message and exit
      -n TOP_N, --top-n TOP_N
                            how many lexical items to compare (default: None)
      -t POS [POS ...], --pos-tags POS [POS ...]
                            a white-list of part-of-speech (POS) tags to include
                            (default: None)
      -k KEY, --key KEY     Rosette API Key (default: None)
      -a API_URL, --api-url API_URL
                            Alternative Rosette API URL (default:
                            https://api.rosette.com/rest/v1/)
    # write out frequency distribution visualization HTML to file
    (compare-vocabulary) $ ./visualize.py data/{carroll,shakespeare} -n 100 -t ADJ ADV > carroll_vs_shakespeare.html

You could then view the HTML file `carroll_vs_shakespeare.html` in your browser of choice.


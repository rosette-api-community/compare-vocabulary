# compare-vocabulary

This repository includes Python examples that leverage the [`/morphology/lemmas` endpoint of Rosette API](https://developer.rosette.com/features-and-functions#morphological-analysis-lemmas) for:

* Comparing vocabulary of vocabulary terms in different sets of documents
* Visualizing frequency distributions of vocabulary terms and their parts-of-speech

## [Jupyter Notebook]((http://nbviewer.jupyter.org/github/zyocum/compare-vocabulary/blob/master/visualize.ipynb))

The simplest way to get started is to access the Jupyter notebook online [**here**](http://nbviewer.jupyter.org/github/zyocum/compare-vocabulary/blob/master/visualize.ipynb).  You can also run the notebook locally (after following [the setup instructions below](https://github.com/zyocum/compare-vocabulary/blob/master/README.md#setup)) by running:

	(compare-vocabulary) $ jupyter notebook visualize.ipynb

You can add to/replace the data directories of plain-text files in the [`data`](https://github.com/zyocum/compare-vocabulary/tree/master/data) directory.  (Some corpora of poems by several famous poets are provided as examples.)

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

    (compare-vocabulary) $ ./compare_vocabulary.py data/{carroll,shakespeare} -n 50 | column -t
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

    (compare-vocabulary) $ ./visualize.py data/{carroll,shakespeare} -n 100 -t ADJ ADV > carroll_vs_shakespeare.html
    

<html>
 <head>
 </head>
 <body>
  <h2>
   Color Key
  </h2>
  <ul>
   <li>
    <font color="#4E8975">
     ADJ:Adjective
    </font>
   </li>
   <li>
    <font color="#A52A2A">
     ADP:Adposition
    </font>
   </li>
   <li>
    <font color="#00FF00">
     ADV:Adverb
    </font>
   </li>
   <li>
    <font color="#0000FF">
     AUX:Auxiliary verb
    </font>
   </li>
   <li>
    <font color="#ff4500">
     CONJ:Coordinating conjunction
    </font>
   </li>
   <li>
    <font color="#c0c0c0">
     DET:Determiner
    </font>
   </li>
   <li>
    <font color="#493D26">
     INTJ:Interjection
    </font>
   </li>
   <li>
    <font color="#FFA500">
     NOUN:Noun
    </font>
   </li>
   <li>
    <font color="#6698FF">
     NUM:Numeral
    </font>
   </li>
   <li>
    <font color="#FF00FF">
     PART:Particle
    </font>
   </li>
   <li>
    <font color="#FF0000">
     PRON:Pronoun
    </font>
   </li>
   <li>
    <font color="#8D38C9">
     PROPN:Proper noun
    </font>
   </li>
   <li>
    <font color="#008080">
     PUNCT:Punctuation
    </font>
   </li>
   <li>
    <font color="#EDDA74">
     SCONJ:Subordinating conjunction
    </font>
   </li>
   <li>
    <font color="#808000">
     SYM:Symbol
    </font>
   </li>
   <li>
    <font color="#800080">
     VERB:Verb
    </font>
   </li>
   <li>
    <font color="#000000">
     X:Other
    </font>
   </li>
  </ul>
  <h1>
   data/carroll
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="so/ADV (7)">
    so
   </font>
   <font color="#00FF00" size="83.5" title="very/ADV (6)">
    very
   </font>
   <font color="#00FF00" size="67.0" title="yet/ADV (5)">
    yet
   </font>
   <font color="#00FF00" size="67.0" title="more/ADV (5)">
    more
   </font>
   <font color="#00FF00" size="50.5" title="how/ADV (4)">
    how
   </font>
   <font color="#4E8975" size="50.5" title="old/ADJ (4)">
    old
   </font>
   <font color="#4E8975" size="50.5" title="good/ADJ (4)">
    good
   </font>
   <font color="#4E8975" size="34.0" title="little/ADJ (3)">
    little
   </font>
   <font color="#00FF00" size="34.0" title="again/ADV (3)">
    again
   </font>
   <font color="#4E8975" size="34.0" title="odd/ADJ (3)">
    odd
   </font>
   <font color="#00FF00" size="34.0" title="there/ADV (3)">
    there
   </font>
   <font color="#4E8975" size="34.0" title="pleasant/ADJ (3)">
    pleasant
   </font>
   <font color="#4E8975" size="17.5" title="young/ADJ (2)">
    young
   </font>
   <font color="#00FF00" size="17.5" title="now/ADV (2)">
    now
   </font>
   <font color="#00FF00" size="17.5" title="why/ADV (2)">
    why
   </font>
   <font color="#00FF00" size="17.5" title="before/ADV (2)">
    before
   </font>
   <font color="#4E8975" size="17.5" title="fat/ADJ (2)">
    fat
   </font>
   <font color="#00FF00" size="17.5" title="too/ADV (2)">
    too
   </font>
   <font color="#00FF00" size="17.5" title="ever/ADV (2)">
    ever
   </font>
   <font color="#4E8975" size="17.5" title="wet/ADJ (2)">
    wet
   </font>
   <font color="#4E8975" size="17.5" title="dry/ADJ (2)">
    dry
   </font>
   <font color="#4E8975" size="17.5" title="eldest/ADJ (2)">
    eldest
   </font>
   <font color="#4E8975" size="17.5" title="thick/ADJ (2)">
    thick
   </font>
   <font color="#4E8975" size="17.5" title="slithy/ADJ (2)">
    slithy
   </font>
   <font color="#4E8975" size="17.5" title="gyre/ADJ (2)">
    gyre
   </font>
   <font color="#4E8975" size="17.5" title="gimble/ADJ (2)">
    gimble
   </font>
   <font color="#4E8975" size="17.5" title="mome/ADJ (2)">
    mome
   </font>
   <font color="#4E8975" size="17.5" title="raths/ADJ (2)">
    raths
   </font>
   <font color="#4E8975" size="17.5" title="vorpal/ADJ (2)">
    vorpal
   </font>
   <font color="#4E8975" size="1.0" title="doth/ADJ (1)">
    doth
   </font>
   <font color="#4E8975" size="1.0" title="golden/ADJ (1)">
    golden
   </font>
   <font color="#00FF00" size="1.0" title="cheerfully/ADV (1)">
    cheerfully
   </font>
   <font color="#00FF00" size="1.0" title="neatly/ADV (1)">
    neatly
   </font>
   <font color="#00FF00" size="1.0" title="gently/ADV (1)">
    gently
   </font>
   <font color="#4E8975" size="1.0" title="white/ADJ (1)">
    white
   </font>
   <font color="#00FF00" size="1.0" title="incessantly/ADV (1)">
    incessantly
   </font>
   <font color="#4E8975" size="1.0" title="right/ADJ (1)">
    right
   </font>
   <font color="#00FF00" size="1.0" title="perfectly/ADV (1)">
    perfectly
   </font>
   <font color="#4E8975" size="1.0" title="sure/ADJ (1)">
    sure
   </font>
   <font color="#00FF00" size="1.0" title="most/ADV (1)">
    most
   </font>
   <font color="#00FF00" size="1.0" title="uncommonly/ADV (1)">
    uncommonly
   </font>
   <font color="#4E8975" size="1.0" title="grey/ADJ (1)">
    grey
   </font>
   <font color="#4E8975" size="1.0" title="supple/ADJ (1)">
    supple
   </font>
   <font color="#4E8975" size="1.0" title="weak/ADJ (1)">
    weak
   </font>
   <font color="#4E8975" size="1.0" title="tough/ADJ (1)">
    tough
   </font>
   <font color="#4E8975" size="1.0" title="muscular/ADJ (1)">
    muscular
   </font>
   <font color="#00FF00" size="1.0" title="hardly/ADV (1)">
    hardly
   </font>
   <font color="#4E8975" size="1.0" title="steady/ADJ (1)">
    steady
   </font>
   <font color="#00FF00" size="1.0" title="awfully/ADV (1)">
    awfully
   </font>
   <font color="#4E8975" size="1.0" title="clever/ADJ (1)">
    clever
   </font>
   <font color="#4E8975" size="1.0" title="off/ADJ (1)">
    off
   </font>
   <font color="#4E8975" size="1.0" title="smooth/ADJ (1)">
    smooth
   </font>
   <font color="#4E8975" size="1.0" title="bright/ADJ (1)">
    bright
   </font>
   <font color="#00FF00" size="1.0" title="sulkily/ADV (1)">
    sulkily
   </font>
   <font color="#4E8975" size="1.0" title="rude/ADJ (1)">
    rude
   </font>
   <font color="#4E8975" size="1.0" title="overhead/ADJ (1)">
    overhead
   </font>
   <font color="#00FF00" size="1.0" title="close/ADV (1)">
    close
   </font>
   <font color="#00FF00" size="1.0" title="only/ADV (1)">
    only
   </font>
   <font color="#00FF00" size="1.0" title="away/ADV (1)">
    away
   </font>
   <font color="#4E8975" size="1.0" title="grand/ADJ (1)">
    grand
   </font>
   <font color="#4E8975" size="1.0" title="clear/ADJ (1)">
    clear
   </font>
   <font color="#4E8975" size="1.0" title="bitter/ADJ (1)">
    bitter
   </font>
   <font color="#4E8975" size="1.0" title="briny/ADJ (1)">
    briny
   </font>
   <font color="#00FF00" size="1.0" title="never/ADV (1)">
    never
   </font>
   <font color="#4E8975" size="1.0" title="heavy/ADJ (1)">
    heavy
   </font>
   <font color="#4E8975" size="1.0" title="eager/ADJ (1)">
    eager
   </font>
   <font color="#4E8975" size="1.0" title="clean/ADJ (1)">
    clean
   </font>
   <font color="#4E8975" size="1.0" title="neat/ADJ (1)">
    neat
   </font>
   <font color="#4E8975" size="1.0" title="other/ADJ (1)">
    other
   </font>
   <font color="#4E8975" size="1.0" title="fast/ADJ (1)">
    fast
   </font>
   <font color="#4E8975" size="1.0" title="last/ADJ (1)">
    last
   </font>
   <font color="#4E8975" size="1.0" title="frothy/ADJ (1)">
    frothy
   </font>
   <font color="#00FF00" size="1.0" title="then/ADV (1)">
    then
   </font>
   <font color="#00FF00" size="1.0" title="conveniently/ADV (1)">
    conveniently
   </font>
   <font color="#4E8975" size="1.0" title="low/ADJ (1)">
    low
   </font>
   <font color="#4E8975" size="1.0" title="hot/ADJ (1)">
    hot
   </font>
   <font color="#00FF00" size="1.0" title="much/ADV (1)">
    much
   </font>
   <font color="#00FF00" size="1.0" title="chiefly/ADV (1)">
    chiefly
   </font>
   <font color="#00FF00" size="1.0" title="indeed/ADV (1)">
    indeed
   </font>
   <font color="#4E8975" size="1.0" title="ready/ADJ (1)">
    ready
   </font>
   <font color="#00FF00" size="1.0" title="little/ADV (1)">
    little
   </font>
   <font color="#4E8975" size="1.0" title="blue/ADJ (1)">
    blue
   </font>
   <font color="#4E8975" size="1.0" title="dismal/ADJ (1)">
    dismal
   </font>
   <font color="#4E8975" size="1.0" title="fine/ADJ (1)">
    fine
   </font>
   <font color="#4E8975" size="1.0" title="kind/ADJ (1)">
    kind
   </font>
   <font color="#4E8975" size="1.0" title="nice/ADJ (1)">
    nice
   </font>
   <font color="#00FF00" size="1.0" title="quite/ADV (1)">
    quite
   </font>
   <font color="#4E8975" size="1.0" title="deaf/ADJ (1)">
    deaf
   </font>
   <font color="#00FF00" size="1.0" title="twice/ADV (1)">
    twice
   </font>
   <font color="#00FF00" size="1.0" title="out/ADV (1)">
    out
   </font>
   <font color="#00FF00" size="1.0" title="far/ADV (1)">
    far
   </font>
   <font color="#4E8975" size="1.0" title="quick/ADJ (1)">
    quick
   </font>
   <font color="#00FF00" size="1.0" title="deeply/ADV (1)">
    deeply
   </font>
   <font color="#4E8975" size="1.0" title="large/ADJ (1)">
    large
   </font>
   <font color="#00FF00" size="1.0" title="scarcely/ADV (1)">
    scarcely
   </font>
   <font color="#4E8975" size="1.0" title="frumious/ADJ (1)">
    frumious
   </font>
   <font color="#4E8975" size="1.0" title="long/ADJ (1)">
    long
   </font>
   <font color="#4E8975" size="1.0" title="manxome/ADJ (1)">
    manxome
   </font>
   <font color="#00FF00" size="1.0" title="awhile/ADV (1)">
    awhile
   </font>
   <font color="#4E8975" size="1.0" title="uffish/ADJ (1)">
    uffish
   </font>
   <font color="#4E8975" size="1.0" title="tulgey/ADJ (1)">
    tulgey
   </font>
   <font color="#00FF00" size="1.0" title="through/ADV (1)">
    through
   </font>
   <font color="#4E8975" size="1.0" title="dead/ADJ (1)">
    dead
   </font>
   <font color="#00FF00" size="1.0" title="back/ADV (1)">
    back
   </font>
   <font color="#4E8975" size="1.0" title="hast/ADJ (1)">
    hast
   </font>
   <font color="#4E8975" size="1.0" title="beamish/ADJ (1)">
    beamish
   </font>
   <font color="#4E8975" size="1.0" title="frabjous/ADJ (1)">
    frabjous
   </font>
   <font color="#4E8975" size="1.0" title="true/ADJ (1)">
    true
   </font>
   <font color="#4E8975" size="1.0" title="free/ADJ (1)">
    free
   </font>
   <font color="#00FF00" size="1.0" title="exactly/ADV (1)">
    exactly
   </font>
   <font color="#4E8975" size="1.0" title="fit/ADJ (1)">
    fit
   </font>
   <font color="#4E8975" size="1.0" title="secret/ADJ (1)">
    secret
   </font>
  </h1>
  <h1>
   data/frost
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="there/ADV (10)">
    there
   </font>
   <font color="#00FF00" size="89.0" title="so/ADV (9)">
    so
   </font>
   <font color="#00FF00" size="67.0" title="where/ADV (7)">
    where
   </font>
   <font color="#4E8975" size="67.0" title="good/ADJ (7)">
    good
   </font>
   <font color="#00FF00" size="34.0" title="only/ADV (4)">
    only
   </font>
   <font color="#00FF00" size="34.0" title="then/ADV (4)">
    then
   </font>
   <font color="#00FF00" size="34.0" title="away/ADV (4)">
    away
   </font>
   <font color="#00FF00" size="34.0" title="again/ADV (4)">
    again
   </font>
   <font color="#00FF00" size="34.0" title="back/ADV (4)">
    back
   </font>
   <font color="#4E8975" size="23.0" title="one/ADJ (3)">
    one
   </font>
   <font color="#00FF00" size="23.0" title="down/ADV (3)">
    down
   </font>
   <font color="#00FF00" size="23.0" title="when/ADV (3)">
    when
   </font>
   <font color="#4E8975" size="23.0" title="dark/ADJ (3)">
    dark
   </font>
   <font color="#00FF00" size="23.0" title="too/ADV (3)">
    too
   </font>
   <font color="#00FF00" size="23.0" title="over/ADV (3)">
    over
   </font>
   <font color="#4E8975" size="12.0" title="gold/ADJ (2)">
    gold
   </font>
   <font color="#00FF00" size="12.0" title="soon/ADV (2)">
    soon
   </font>
   <font color="#00FF00" size="12.0" title="never/ADV (2)">
    never
   </font>
   <font color="#00FF00" size="12.0" title="out/ADV (2)">
    out
   </font>
   <font color="#00FF00" size="12.0" title="far/ADV (2)">
    far
   </font>
   <font color="#4E8975" size="12.0" title="same/ADJ (2)">
    same
   </font>
   <font color="#00FF00" size="12.0" title="even/ADV (2)">
    even
   </font>
   <font color="#00FF00" size="12.0" title="once/ADV (2)">
    once
   </font>
   <font color="#00FF00" size="12.0" title="well/ADV (2)">
    well
   </font>
   <font color="#4E8975" size="12.0" title="black/ADJ (2)">
    black
   </font>
   <font color="#00FF00" size="12.0" title="more/ADV (2)">
    more
   </font>
   <font color="#4E8975" size="12.0" title="frozen/ADJ (2)">
    frozen
   </font>
   <font color="#00FF00" size="12.0" title="just/ADV (2)">
    just
   </font>
   <font color="#00FF00" size="12.0" title="here/ADV (2)">
    here
   </font>
   <font color="#4E8975" size="12.0" title="other/ADJ (2)">
    other
   </font>
   <font color="#4E8975" size="1.0" title="green/ADJ (1)">
    green
   </font>
   <font color="#4E8975" size="1.0" title="hard/ADJ (1)">
    hard
   </font>
   <font color="#4E8975" size="1.0" title="early/ADJ (1)">
    early
   </font>
   <font color="#00FF00" size="1.0" title="twice/ADV (1)">
    twice
   </font>
   <font color="#00FF00" size="1.0" title="also/ADV (1)">
    also
   </font>
   <font color="#4E8975" size="1.0" title="great/ADJ (1)">
    great
   </font>
   <font color="#4E8975" size="1.0" title="straight/ADJ (1)">
    straight
   </font>
   <font color="#00FF00" size="1.0" title="often/ADV (1)">
    often
   </font>
   <font color="#4E8975" size="1.0" title="sunny/ADJ (1)">
    sunny
   </font>
   <font color="#4E8975" size="1.0" title="inner/ADJ (1)">
    inner
   </font>
   <font color="#4E8975" size="1.0" title="withered/ADJ (1)">
    withered
   </font>
   <font color="#4E8975" size="1.0" title="low/ADJ (1)">
    low
   </font>
   <font color="#4E8975" size="1.0" title="long/ADJ (1)">
    long
   </font>
   <font color="#00FF00" size="1.0" title="right/ADV (1)">
    right
   </font>
   <font color="#00FF00" size="1.0" title="afterwards/ADV (1)">
    afterwards
   </font>
   <font color="#00FF00" size="1.0" title="alone/ADV (1)">
    alone
   </font>
   <font color="#4E8975" size="1.0" title="clear/ADJ (1)">
    clear
   </font>
   <font color="#00FF00" size="1.0" title="always/ADV (1)">
    always
   </font>
   <font color="#4E8975" size="1.0" title="top/ADJ (1)">
    top
   </font>
   <font color="#00FF00" size="1.0" title="carefully/ADV (1)">
    carefully
   </font>
   <font color="#00FF00" size="1.0" title="outward/ADV (1)">
    outward
   </font>
   <font color="#4E8975" size="1.0" title="weary/ADJ (1)">
    weary
   </font>
   <font color="#00FF00" size="1.0" title="much/ADV (1)">
    much
   </font>
   <font color="#4E8975" size="1.0" title="pathless/ADJ (1)">
    pathless
   </font>
   <font color="#4E8975" size="1.0" title="open/ADJ (1)">
    open
   </font>
   <font color="#00FF00" size="1.0" title="awhile/ADV (1)">
    awhile
   </font>
   <font color="#00FF00" size="1.0" title="willfully/ADV (1)">
    willfully
   </font>
   <font color="#4E8975" size="1.0" title="right/ADJ (1)">
    right
   </font>
   <font color="#4E8975" size="1.0" title="likely/ADJ (1)">
    likely
   </font>
   <font color="#4E8975" size="1.0" title="white/ADJ (1)">
    white
   </font>
   <font color="#00FF00" size="1.0" title="bad/ADV (1)">
    bad
   </font>
   <font color="#4E8975" size="1.0" title="upper/ADJ (1)">
    upper
   </font>
   <font color="#00FF00" size="1.0" title="abreast/ADV (1)">
    abreast
   </font>
   <font color="#00FF00" size="1.0" title="nearly/ADV (1)">
    nearly
   </font>
   <font color="#4E8975" size="1.0" title="rough/ADJ (1)">
    rough
   </font>
   <font color="#00FF00" size="1.0" title="little/ADV (1)">
    little
   </font>
   <font color="#00FF00" size="1.0" title="why/ADV (1)">
    why
   </font>
   <font color="#00FF00" size="1.0" title="exactly/ADV (1)">
    exactly
   </font>
   <font color="#00FF00" size="1.0" title="rather/ADV (1)">
    rather
   </font>
   <font color="#00FF00" size="1.0" title="firmly/ADV (1)">
    firmly
   </font>
   <font color="#4E8975" size="1.0" title="old/ADJ (1)">
    old
   </font>
   <font color="#00FF00" size="1.0" title="though/ADV (1)">
    though
   </font>
   <font color="#4E8975" size="1.0" title="little/ADJ (1)">
    little
   </font>
   <font color="#4E8975" size="1.0" title="queer/ADJ (1)">
    queer
   </font>
   <font color="#00FF00" size="1.0" title="near/ADV (1)">
    near
   </font>
   <font color="#4E8975" size="1.0" title="only/ADJ (1)">
    only
   </font>
   <font color="#4E8975" size="1.0" title="easy/ADJ (1)">
    easy
   </font>
   <font color="#4E8975" size="1.0" title="downy/ADJ (1)">
    downy
   </font>
   <font color="#4E8975" size="1.0" title="lovely/ADJ (1)">
    lovely
   </font>
   <font color="#4E8975" size="1.0" title="deep/ADJ (1)">
    deep
   </font>
   <font color="#4E8975" size="1.0" title="yellow/ADJ (1)">
    yellow
   </font>
   <font color="#4E8975" size="1.0" title="sorry/ADJ (1)">
    sorry
   </font>
   <font color="#00FF00" size="1.0" title="long/ADV (1)">
    long
   </font>
   <font color="#4E8975" size="1.0" title="fair/ADJ (1)">
    fair
   </font>
   <font color="#00FF00" size="1.0" title="perhaps/ADV (1)">
    perhaps
   </font>
   <font color="#4E8975" size="1.0" title="grassy/ADJ (1)">
    grassy
   </font>
   <font color="#00FF00" size="1.0" title="really/ADV (1)">
    really
   </font>
   <font color="#00FF00" size="1.0" title="about/ADV (1)">
    about
   </font>
   <font color="#00FF00" size="1.0" title="equally/ADV (1)">
    equally
   </font>
   <font color="#00FF00" size="1.0" title="yet/ADV (1)">
    yet
   </font>
   <font color="#00FF00" size="1.0" title="how/ADV (1)">
    how
   </font>
   <font color="#00FF00" size="1.0" title="ever/ADV (1)">
    ever
   </font>
   <font color="#00FF00" size="1.0" title="somewhere/ADV (1)">
    somewhere
   </font>
   <font color="#00FF00" size="1.0" title="hence/ADV (1)">
    hence
   </font>
   <font color="#00FF00" size="1.0" title="less/ADV (1)">
    less
   </font>
  </h1>
  <h1>
   data/poe
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="there/ADV (16)">
    there
   </font>
   <font color="#00FF00" size="93.39999999999999" title="so/ADV (15)">
    so
   </font>
   <font color="#00FF00" size="93.39999999999999" title="more/ADV (15)">
    more
   </font>
   <font color="#00FF00" size="73.6" title="nevermore/ADV (12)">
    nevermore
   </font>
   <font color="#00FF00" size="67.0" title="then/ADV (11)">
    then
   </font>
   <font color="#00FF00" size="47.199999999999996" title="here/ADV (8)">
    here
   </font>
   <font color="#00FF00" size="47.199999999999996" title="where/ADV (8)">
    where
   </font>
   <font color="#00FF00" size="47.199999999999996" title="still/ADV (8)">
    still
   </font>
   <font color="#00FF00" size="40.599999999999994" title="now/ADV (7)">
    now
   </font>
   <font color="#00FF00" size="40.599999999999994" title="far/ADV (7)">
    far
   </font>
   <font color="#00FF00" size="27.4" title="ever/ADV (5)">
    ever
   </font>
   <font color="#00FF00" size="27.4" title="never/ADV (5)">
    never
   </font>
   <font color="#4E8975" size="20.799999999999997" title="sad/ADJ (4)">
    sad
   </font>
   <font color="#00FF00" size="20.799999999999997" title="when/ADV (4)">
    when
   </font>
   <font color="#00FF00" size="20.799999999999997" title="how/ADV (4)">
    how
   </font>
   <font color="#4E8975" size="20.799999999999997" title="other/ADJ (4)">
    other
   </font>
   <font color="#00FF00" size="20.799999999999997" title="long/ADV (4)">
    long
   </font>
   <font color="#4E8975" size="20.799999999999997" title="beautiful/ADJ (4)">
    beautiful
   </font>
   <font color="#4E8975" size="14.2" title="sure/ADJ (3)">
    sure
   </font>
   <font color="#4E8975" size="14.2" title="golden/ADJ (3)">
    golden
   </font>
   <font color="#4E8975" size="14.2" title="dead/ADJ (3)">
    dead
   </font>
   <font color="#4E8975" size="14.2" title="young/ADJ (3)">
    young
   </font>
   <font color="#00FF00" size="14.2" title="before/ADV (3)">
    before
   </font>
   <font color="#4E8975" size="14.2" title="old/ADJ (3)">
    old
   </font>
   <font color="#00FF00" size="14.2" title="alone/ADV (3)">
    alone
   </font>
   <font color="#4E8975" size="14.2" title="good/ADJ (3)">
    good
   </font>
   <font color="#4E8975" size="14.2" title="happy/ADJ (3)">
    happy
   </font>
   <font color="#00FF00" size="14.2" title="back/ADV (3)">
    back
   </font>
   <font color="#4E8975" size="7.6" title="weary/ADJ (2)">
    weary
   </font>
   <font color="#4E8975" size="7.6" title="grey/ADJ (2)">
    grey
   </font>
   <font color="#4E8975" size="7.6" title="loud/ADJ (2)">
    loud
   </font>
   <font color="#00FF00" size="7.6" title="forever/ADV (2)">
    forever
   </font>
   <font color="#4E8975" size="7.6" title="pallid/ADJ (2)">
    pallid
   </font>
   <font color="#4E8975" size="7.6" title="high/ADJ (2)">
    high
   </font>
   <font color="#4E8975" size="7.6" title="saintly/ADJ (2)">
    saintly
   </font>
   <font color="#4E8975" size="7.6" title="low/ADJ (2)">
    low
   </font>
   <font color="#00FF00" size="7.6" title="thus/ADV (2)">
    thus
   </font>
   <font color="#00FF00" size="7.6" title="avaunt/ADV (2)">
    avaunt
   </font>
   <font color="#4E8975" size="7.6" title="light/ADJ (2)">
    light
   </font>
   <font color="#4E8975" size="7.6" title="same/ADJ (2)">
    same
   </font>
   <font color="#4E8975" size="7.6" title="red/ADJ (2)">
    red
   </font>
   <font color="#4E8975" size="7.6" title="green/ADJ (2)">
    green
   </font>
   <font color="#4E8975" size="7.6" title="bright/ADJ (2)">
    bright
   </font>
   <font color="#4E8975" size="7.6" title="dim/ADJ (2)">
    dim
   </font>
   <font color="#4E8975" size="7.6" title="eternal/ADJ (2)">
    eternal
   </font>
   <font color="#4E8975" size="7.6" title="dull/ADJ (2)">
    dull
   </font>
   <font color="#4E8975" size="7.6" title="wise/ADJ (2)">
    wise
   </font>
   <font color="#4E8975" size="7.6" title="undaunted/ADJ (2)">
    undaunted
   </font>
   <font color="#4E8975" size="7.6" title="bad/ADJ (2)">
    bad
   </font>
   <font color="#00FF00" size="7.6" title="resignedly/ADV (2)">
    resignedly
   </font>
   <font color="#4E8975" size="7.6" title="long/ADJ (2)">
    long
   </font>
   <font color="#4E8975" size="7.6" title="sculptured/ADJ (2)">
    sculptured
   </font>
   <font color="#00FF00" size="7.6" title="ago/ADV (2)">
    ago
   </font>
   <font color="#4E8975" size="7.6" title="strong/ADJ (2)">
    strong
   </font>
   <font color="#00FF00" size="7.6" title="gently/ADV (2)">
    gently
   </font>
   <font color="#00FF00" size="7.6" title="only/ADV (2)">
    only
   </font>
   <font color="#4E8975" size="7.6" title="rare/ADJ (2)">
    rare
   </font>
   <font color="#4E8975" size="7.6" title="radiant/ADJ (2)">
    radiant
   </font>
   <font color="#4E8975" size="7.6" title="visiter/ADJ (2)">
    visiter
   </font>
   <font color="#00FF00" size="7.6" title="truely/ADV (2)">
    truely
   </font>
   <font color="#4E8975" size="7.6" title="unbroken/ADJ (2)">
    unbroken
   </font>
   <font color="#4E8975" size="7.6" title="only/ADJ (2)">
    only
   </font>
   <font color="#00FF00" size="7.6" title="surely/ADV (2)">
    surely
   </font>
   <font color="#00FF00" size="7.6" title="just/ADV (2)">
    just
   </font>
   <font color="#4E8975" size="7.6" title="grim/ADJ (2)">
    grim
   </font>
   <font color="#4E8975" size="7.6" title="plutonian/ADJ (2)">
    plutonian
   </font>
   <font color="#4E8975" size="7.6" title="ungainly/ADJ (2)">
    ungainly
   </font>
   <font color="#4E8975" size="7.6" title="little/ADJ (2)">
    little
   </font>
   <font color="#00FF00" size="7.6" title="yet/ADV (2)">
    yet
   </font>
   <font color="#00FF00" size="7.6" title="fast/ADV (2)">
    fast
   </font>
   <font color="#4E8975" size="7.6" title="ominous/ADJ (2)">
    ominous
   </font>
   <font color="#4E8975" size="1.0" title="antique/ADJ (1)">
    antique
   </font>
   <font color="#4E8975" size="1.0" title="rich/ADJ (1)">
    rich
   </font>
   <font color="#4E8975" size="1.0" title="lofty/ADJ (1)">
    lofty
   </font>
   <font color="#4E8975" size="1.0" title="humble/ADJ (1)">
    humble
   </font>
   <font color="#4E8975" size="1.0" title="very/ADJ (1)">
    very
   </font>
   <font color="#4E8975" size="1.0" title="e'er/ADJ (1)">
    e'er
   </font>
   <font color="#4E8975" size="1.0" title="judaean/ADJ (1)">
    judaean
   </font>
   <font color="#4E8975" size="1.0" title="potent/ADJ (1)">
    potent
   </font>
   <font color="#4E8975" size="1.0" title="rapt/ADJ (1)">
    rapt
   </font>
   <font color="#4E8975" size="1.0" title="quiet/ADJ (1)">
    quiet
   </font>
   <font color="#4E8975" size="1.0" title="swarthy/ADJ (1)">
    swarthy
   </font>
   <font color="#4E8975" size="1.0" title="gilded/ADJ (1)">
    gilded
   </font>
   <font color="#4E8975" size="1.0" title="wan/ADJ (1)">
    wan
   </font>
   <font color="#4E8975" size="1.0" title="horned/ADJ (1)">
    horned
   </font>
   <font color="#4E8975" size="1.0" title="swift/ADJ (1)">
    swift
   </font>
   <font color="#4E8975" size="1.0" title="silent/ADJ (1)">
    silent
   </font>
   <font color="#4E8975" size="1.0" title="clad/ADJ (1)">
    clad
   </font>
   <font color="#4E8975" size="1.0" title="blackened/ADJ (1)">
    blackened
   </font>
   <font color="#4E8975" size="1.0" title="vague/ADJ (1)">
    vague
   </font>
   <font color="#4E8975" size="1.0" title="famed/ADJ (1)">
    famed
   </font>
   <font color="#4E8975" size="1.0" title="colossal/ADJ (1)">
    colossal
   </font>
   <font color="#4E8975" size="1.0" title="corrosive/ADJ (1)">
    corrosive
   </font>
   <font color="#4E8975" size="1.0" title="prophetic/ADJ (1)">
    prophetic
   </font>
   <font color="#4E8975" size="1.0" title="mighty/ADJ (1)">
    mighty
   </font>
   <font color="#4E8975" size="1.0" title="despotic/ADJ (1)">
    despotic
   </font>
   <font color="#4E8975" size="1.0" title="giant/ADJ (1)">
    giant
   </font>
   <font color="#4E8975" size="1.0" title="impotent/ADJ (1)">
    impotent
   </font>
   <font color="#00FF00" size="1.0" title="around/ADV (1)">
    around
   </font>
   <font color="#4E8975" size="1.0" title="stygian/ADJ (1)">
    stygian
   </font>
   <font color="#4E8975" size="1.0" title="hast/ADJ (1)">
    hast
   </font>
   <font color="#00FF00" size="1.0" title="yon/ADV (1)">
    yon
   </font>
   <font color="#4E8975" size="1.0" title="drear/ADJ (1)">
    drear
   </font>
   <font color="#4E8975" size="1.0" title="rigid/ADJ (1)">
    rigid
   </font>
   <font color="#4E8975" size="1.0" title="queenly/ADJ (1)">
    queenly
   </font>
   <font color="#00FF00" size="1.0" title="doubly/ADV (1)">
    doubly
   </font>
   <font color="#4E8975" size="1.0" title="feeble/ADJ (1)">
    feeble
   </font>
   <font color="#4E8975" size="1.0" title="evil/ADJ (1)">
    evil
   </font>
   <font color="#4E8975" size="1.0" title="slanderous/ADJ (1)">
    slanderous
   </font>
   <font color="#00FF00" size="1.0" title="solemnly/ADV (1)">
    solemnly
   </font>
   <font color="#4E8975" size="1.0" title="sweet/ADJ (1)">
    sweet
   </font>
   <font color="#4E8975" size="1.0" title="wild/ADJ (1)">
    wild
   </font>
   <font color="#4E8975" size="1.0" title="dear/ADJ (1)">
    dear
   </font>
   <font color="#4E8975" size="1.0" title="fair/ADJ (1)">
    fair
   </font>
   <font color="#4E8975" size="1.0" title="debonair/ADJ (1)">
    debonair
   </font>
   <font color="#4E8975" size="1.0" title="lowly/ADJ (1)">
    lowly
   </font>
   <font color="#4E8975" size="1.0" title="yellow/ADJ (1)">
    yellow
   </font>
   <font color="#4E8975" size="1.0" title="indignant/ADJ (1)">
    indignant
   </font>
   <font color="#4E8975" size="1.0" title="riven/ADJ (1)">
    riven
   </font>
   <font color="#4E8975" size="1.0" title="hallowed/ADJ (1)">
    hallowed
   </font>
   <font color="#00FF00" size="1.0" title="up/ADV (1)">
    up
   </font>
   <font color="#4E8975" size="1.0" title="damned/ADJ (1)">
    damned
   </font>
   <font color="#4E8975" size="1.0" title="common/ADJ (1)">
    common
   </font>
   <font color="#00FF00" size="1.0" title="most/ADV (1)">
    most
   </font>
   <font color="#4E8975" size="1.0" title="stormy/ADJ (1)">
    stormy
   </font>
   <font color="#4E8975" size="1.0" title="ill/ADJ (1)">
    ill
   </font>
   <font color="#4E8975" size="1.0" title="blue/ADJ (1)">
    blue
   </font>
   <font color="#4E8975" size="1.0" title="wast/ADJ (1)">
    wast
   </font>
   <font color="#00FF00" size="1.0" title="too/ADV (1)">
    too
   </font>
   <font color="#4E8975" size="1.0" title="starry/ADJ (1)">
    starry
   </font>
   <font color="#4E8975" size="1.0" title="future/ADJ (1)">
    future
   </font>
   <font color="#00FF00" size="1.0" title="on/ADV (1)">
    on
   </font>
   <font color="#4E8975" size="1.0" title="mute/ADJ (1)">
    mute
   </font>
   <font color="#4E8975" size="1.0" title="motionless/ADJ (1)">
    motionless
   </font>
   <font color="#4E8975" size="1.0" title="aghast/ADJ (1)">
    aghast
   </font>
   <font color="#4E8975" size="1.0" title="solemn/ADJ (1)">
    solemn
   </font>
   <font color="#4E8975" size="1.0" title="blasted/ADJ (1)">
    blasted
   </font>
   <font color="#4E8975" size="1.0" title="strikeed/ADJ (1)">
    strikeed
   </font>
   <font color="#4E8975" size="1.0" title="nightly/ADJ (1)">
    nightly
   </font>
   <font color="#4E8975" size="1.0" title="ethereal/ADJ (1)">
    ethereal
   </font>
   <font color="#4E8975" size="1.0" title="true/ADJ (1)">
    true
   </font>
   <font color="#4E8975" size="1.0" title="alterest/ADJ (1)">
    alterest
   </font>
   <font color="#00FF00" size="1.0" title="why/ADV (1)">
    why
   </font>
   <font color="#4E8975" size="1.0" title="preyest/ADJ (1)">
    preyest
   </font>
   <font color="#4E8975" size="1.0" title="wouldst/ADJ (1)">
    wouldst
   </font>
   <font color="#4E8975" size="1.0" title="jewelled/ADJ (1)">
    jewelled
   </font>
   <font color="#4E8975" size="1.0" title="gallant/ADJ (1)">
    gallant
   </font>
   <font color="#4E8975" size="1.0" title="bold/ADJ (1)">
    bold
   </font>
   <font color="#00FF00" size="1.0" title="boldly/ADV (1)">
    boldly
   </font>
   <font color="#4E8975" size="1.0" title="strange/ADJ (1)">
    strange
   </font>
   <font color="#4E8975" size="1.0" title="holy/ADJ (1)">
    holy
   </font>
   <font color="#4E8975" size="1.0" title="lurid/ADJ (1)">
    lurid
   </font>
   <font color="#00FF00" size="1.0" title="silently/ADV (1)">
    silently
   </font>
   <font color="#4E8975" size="1.0" title="free/ADJ (1)">
    free
   </font>
   <font color="#4E8975" size="1.0" title="up/ADJ (1)">
    up
   </font>
   <font color="#4E8975" size="1.0" title="kingly/ADJ (1)">
    kingly
   </font>
   <font color="#4E8975" size="1.0" title="shadowy/ADJ (1)">
    shadowy
   </font>
   <font color="#4E8975" size="1.0" title="marvelous/ADJ (1)">
    marvelous
   </font>
   <font color="#4E8975" size="1.0" title="pendulous/ADJ (1)">
    pendulous
   </font>
   <font color="#4E8975" size="1.0" title="proud/ADJ (1)">
    proud
   </font>
   <font color="#00FF00" size="1.0" title="gigantically/ADV (1)">
    gigantically
   </font>
   <font color="#4E8975" size="1.0" title="open/ADJ (1)">
    open
   </font>
   <font color="#4E8975" size="1.0" title="luminous/ADJ (1)">
    luminous
   </font>
   <font color="#4E8975" size="1.0" title="gaily/ADJ (1)">
    gaily
   </font>
   <font color="#00FF00" size="1.0" title="less/ADV (1)">
    less
   </font>
   <font color="#00FF00" size="1.0" title="hideously/ADV (1)">
    hideously
   </font>
   <font color="#4E8975" size="1.0" title="serene/ADJ (1)">
    serene
   </font>
   <font color="#00FF00" size="1.0" title="aside/ADV (1)">
    aside
   </font>
   <font color="#00FF00" size="1.0" title="slightly/ADV (1)">
    slightly
   </font>
   <font color="#00FF00" size="1.0" title="feebly/ADV (1)">
    feebly
   </font>
   <font color="#4E8975" size="1.0" title="filmy/ADJ (1)">
    filmy
   </font>
   <font color="#4E8975" size="1.0" title="faint/ADJ (1)">
    faint
   </font>
   <font color="#4E8975" size="1.0" title="earthly/ADJ (1)">
    earthly
   </font>
   <font color="#00FF00" size="1.0" title="hence/ADV (1)">
    hence
   </font>
   <font color="#4E8975" size="1.0" title="winged/ADJ (1)">
    winged
   </font>
   <font color="#4E8975" size="1.0" title="highborn/ADJ (1)">
    highborn
   </font>
   <font color="#00FF00" size="1.0" title="away/ADV (1)">
    away
   </font>
   <font color="#00FF00" size="1.0" title="yes/ADV (1)">
    yes
   </font>
   <font color="#4E8975" size="1.0" title="above/ADJ (1)">
    above
   </font>
   <font color="#00FF00" size="1.0" title="once/ADV (1)">
    once
   </font>
   <font color="#4E8975" size="1.0" title="dreary/ADJ (1)">
    dreary
   </font>
   <font color="#4E8975" size="1.0" title="weak/ADJ (1)">
    weak
   </font>
   <font color="#4E8975" size="1.0" title="quaint/ADJ (1)">
    quaint
   </font>
   <font color="#4E8975" size="1.0" title="curious/ADJ (1)">
    curious
   </font>
   <font color="#00FF00" size="1.0" title="nearly/ADV (1)">
    nearly
   </font>
   <font color="#00FF00" size="1.0" title="suddenly/ADV (1)">
    suddenly
   </font>
   <font color="#00FF00" size="1.0" title="distinctly/ADV (1)">
    distinctly
   </font>
   <font color="#4E8975" size="1.0" title="bleak/ADJ (1)">
    bleak
   </font>
   <font color="#4E8975" size="1.0" title="separate/ADJ (1)">
    separate
   </font>
   <font color="#4E8975" size="1.0" title="wrought/ADJ (1)">
    wrought
   </font>
   <font color="#00FF00" size="1.0" title="eagerly/ADV (1)">
    eagerly
   </font>
   <font color="#00FF00" size="1.0" title="vainly/ADV (1)">
    vainly
   </font>
   <font color="#00FF00" size="1.0" title="evermore/ADV (1)">
    evermore
   </font>
   <font color="#4E8975" size="1.0" title="silken/ADJ (1)">
    silken
   </font>
   <font color="#4E8975" size="1.0" title="uncertain/ADJ (1)">
    uncertain
   </font>
   <font color="#4E8975" size="1.0" title="purple/ADJ (1)">
    purple
   </font>
   <font color="#4E8975" size="1.0" title="fantastic/ADJ (1)">
    fantastic
   </font>
   <font color="#4E8975" size="1.0" title="late/ADJ (1)">
    late
   </font>
   <font color="#00FF00" size="1.0" title="presently/ADV (1)">
    presently
   </font>
   <font color="#00FF00" size="1.0" title="no/ADV (1)">
    no
   </font>
   <font color="#00FF00" size="1.0" title="faintly/ADV (1)">
    faintly
   </font>
   <font color="#4E8975" size="1.0" title="scarce/ADJ (1)">
    scarce
   </font>
   <font color="#4E8975" size="1.0" title="wide/ADJ (1)">
    wide
   </font>
   <font color="#4E8975" size="1.0" title="whispered/ADJ (1)">
    whispered
   </font>
   <font color="#00FF00" size="1.0" title="merely/ADV (1)">
    merely
   </font>
   <font color="#4E8975" size="1.0" title="sour/ADJ (1)">
    sour
   </font>
   <font color="#00FF00" size="1.0" title="soon/ADV (1)">
    soon
   </font>
   <font color="#00FF00" size="1.0" title="again/ADV (1)">
    again
   </font>
   <font color="#00FF00" size="1.0" title="thereat/ADV (1)">
    thereat
   </font>
   <font color="#4E8975" size="1.0" title="stately/ADJ (1)">
    stately
   </font>
   <font color="#00FF00" size="1.0" title="least/ADV (1)">
    least
   </font>
   <font color="#4E8975" size="1.0" title="ebony/ADJ (1)">
    ebony
   </font>
   <font color="#4E8975" size="1.0" title="grave/ADJ (1)">
    grave
   </font>
   <font color="#4E8975" size="1.0" title="stern/ADJ (1)">
    stern
   </font>
   <font color="#4E8975" size="1.0" title="shaven/ADJ (1)">
    shaven
   </font>
   <font color="#4E8975" size="1.0" title="ancient/ADJ (1)">
    ancient
   </font>
   <font color="#4E8975" size="1.0" title="lordly/ADJ (1)">
    lordly
   </font>
   <font color="#00FF00" size="1.0" title="much/ADV (1)">
    much
   </font>
   <font color="#00FF00" size="1.0" title="plainly/ADV (1)">
    plainly
   </font>
   <font color="#00FF00" size="1.0" title="lonely/ADV (1)">
    lonely
   </font>
   <font color="#4E8975" size="1.0" title="placid/ADJ (1)">
    placid
   </font>
   <font color="#00FF00" size="1.0" title="scarcely/ADV (1)">
    scarcely
   </font>
   <font color="#00FF00" size="1.0" title="aptly/ADV (1)">
    aptly
   </font>
   <font color="#4E8975" size="1.0" title="doubtless/ADJ (1)">
    doubtless
   </font>
   <font color="#4E8975" size="1.0" title="unhappy/ADJ (1)">
    unhappy
   </font>
   <font color="#4E8975" size="1.0" title="unmerciful/ADJ (1)">
    unmerciful
   </font>
   <font color="#4E8975" size="1.0" title="melancholy/ADJ (1)">
    melancholy
   </font>
   <font color="#4E8975" size="1.0" title="velvet/ADJ (1)">
    velvet
   </font>
   <font color="#4E8975" size="1.0" title="ghastly/ADJ (1)">
    ghastly
   </font>
   <font color="#4E8975" size="1.0" title="gaunt/ADJ (1)">
    gaunt
   </font>
   <font color="#4E8975" size="1.0" title="fiery/ADJ (1)">
    fiery
   </font>
   <font color="#00FF00" size="1.0" title="o'er/ADV (1)">
    o'er
   </font>
   <font color="#4E8975" size="1.0" title="dense/ADJ (1)">
    dense
   </font>
   <font color="#4E8975" size="1.0" title="unseen/ADJ (1)">
    unseen
   </font>
   <font color="#4E8975" size="1.0" title="tufted/ADJ (1)">
    tufted
   </font>
   <font color="#4E8975" size="1.0" title="kind/ADJ (1)">
    kind
   </font>
   <font color="#00FF00" size="1.0" title="ashore/ADV (1)">
    ashore
   </font>
   <font color="#4E8975" size="1.0" title="laden/ADJ (1)">
    laden
   </font>
   <font color="#4E8975" size="1.0" title="distant/ADJ (1)">
    distant
   </font>
   <font color="#4E8975" size="1.0" title="black/ADJ (1)">
    black
   </font>
   <font color="#4E8975" size="1.0" title="flitting/ADJ (1)">
    flitting
   </font>
   <font color="#4E8975" size="1.0" title="streaming/ADJ (1)">
    streaming
   </font>
  </h1>
  <h1>
   data/shakespeare
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="more/ADV (7)">
    more
   </font>
   <font color="#00FF00" size="83.5" title="when/ADV (6)">
    when
   </font>
   <font color="#00FF00" size="50.5" title="long/ADV (4)">
    long
   </font>
   <font color="#00FF00" size="34.0" title="so/ADV (3)">
    so
   </font>
   <font color="#00FF00" size="34.0" title="then/ADV (3)">
    then
   </font>
   <font color="#00FF00" size="34.0" title="never/ADV (3)">
    never
   </font>
   <font color="#4E8975" size="17.5" title="gilded/ADJ (2)">
    gilded
   </font>
   <font color="#4E8975" size="17.5" title="tired/ADJ (2)">
    tired
   </font>
   <font color="#4E8975" size="17.5" title="sweet/ADJ (2)">
    sweet
   </font>
   <font color="#4E8975" size="17.5" title="new/ADJ (2)">
    new
   </font>
   <font color="#4E8975" size="17.5" title="dear/ADJ (2)">
    dear
   </font>
   <font color="#4E8975" size="17.5" title="hath/ADJ (2)">
    hath
   </font>
   <font color="#00FF00" size="17.5" title="too/ADV (2)">
    too
   </font>
   <font color="#4E8975" size="17.5" title="fair/ADJ (2)">
    fair
   </font>
   <font color="#4E8975" size="17.5" title="eternal/ADJ (2)">
    eternal
   </font>
   <font color="#4E8975" size="17.5" title="black/ADJ (2)">
    black
   </font>
   <font color="#00FF00" size="17.5" title="ever/ADV (2)">
    ever
   </font>
   <font color="#00FF00" size="17.5" title="far/ADV (2)">
    far
   </font>
   <font color="#4E8975" size="17.5" title="red/ADJ (2)">
    red
   </font>
   <font color="#4E8975" size="17.5" title="white/ADJ (2)">
    white
   </font>
   <font color="#00FF00" size="17.5" title="yet/ADV (2)">
    yet
   </font>
   <font color="#4E8975" size="1.0" title="powerful/ADJ (1)">
    powerful
   </font>
   <font color="#4E8975" size="1.0" title="bright/ADJ (1)">
    bright
   </font>
   <font color="#4E8975" size="1.0" title="unswept/ADJ (1)">
    unswept
   </font>
   <font color="#4E8975" size="1.0" title="sluttish/ADJ (1)">
    sluttish
   </font>
   <font color="#4E8975" size="1.0" title="wasteful/ADJ (1)">
    wasteful
   </font>
   <font color="#4E8975" size="1.0" title="quick/ADJ (1)">
    quick
   </font>
   <font color="#4E8975" size="1.0" title="gainst/ADJ (1)">
    gainst
   </font>
   <font color="#4E8975" size="1.0" title="oblivious/ADJ (1)">
    oblivious
   </font>
   <font color="#00FF00" size="1.0" title="forth/ADV (1)">
    forth
   </font>
   <font color="#00FF00" size="1.0" title="still/ADV (1)">
    still
   </font>
   <font color="#00FF00" size="1.0" title="even/ADV (1)">
    even
   </font>
   <font color="#4E8975" size="1.0" title="restful/ADJ (1)">
    restful
   </font>
   <font color="#4E8975" size="1.0" title="born/ADJ (1)">
    born
   </font>
   <font color="#4E8975" size="1.0" title="needy/ADJ (1)">
    needy
   </font>
   <font color="#4E8975" size="1.0" title="pure/ADJ (1)">
    pure
   </font>
   <font color="#00FF00" size="1.0" title="unhappily/ADV (1)">
    unhappily
   </font>
   <font color="#00FF00" size="1.0" title="shamefully/ADV (1)">
    shamefully
   </font>
   <font color="#4E8975" size="1.0" title="maiden/ADJ (1)">
    maiden
   </font>
   <font color="#00FF00" size="1.0" title="rudely/ADV (1)">
    rudely
   </font>
   <font color="#4E8975" size="1.0" title="right/ADJ (1)">
    right
   </font>
   <font color="#00FF00" size="1.0" title="wrongfully/ADV (1)">
    wrongfully
   </font>
   <font color="#4E8975" size="1.0" title="disabled/ADJ (1)">
    disabled
   </font>
   <font color="#4E8975" size="1.0" title="controlling/ADJ (1)">
    controlling
   </font>
   <font color="#4E8975" size="1.0" title="simple/ADJ (1)">
    simple
   </font>
   <font color="#4E8975" size="1.0" title="captive/ADJ (1)">
    captive
   </font>
   <font color="#4E8975" size="1.0" title="good/ADJ (1)">
    good
   </font>
   <font color="#4E8975" size="1.0" title="ill/ADJ (1)">
    ill
   </font>
   <font color="#00FF00" size="1.0" title="alone/ADV (1)">
    alone
   </font>
   <font color="#4E8975" size="1.0" title="silent/ADJ (1)">
    silent
   </font>
   <font color="#4E8975" size="1.0" title="old/ADJ (1)">
    old
   </font>
   <font color="#4E8975" size="1.0" title="unused/ADJ (1)">
    unused
   </font>
   <font color="#4E8975" size="1.0" title="precious/ADJ (1)">
    precious
   </font>
   <font color="#4E8975" size="1.0" title="dateless/ADJ (1)">
    dateless
   </font>
   <font color="#00FF00" size="1.0" title="afresh/ADV (1)">
    afresh
   </font>
   <font color="#00FF00" size="1.0" title="heavily/ADV (1)">
    heavily
   </font>
   <font color="#4E8975" size="1.0" title="sad/ADJ (1)">
    sad
   </font>
   <font color="#4E8975" size="1.0" title="fore/ADJ (1)">
    fore
   </font>
   <font color="#4E8975" size="1.0" title="bemoaned/ADJ (1)">
    bemoaned
   </font>
   <font color="#4E8975" size="1.0" title="lovely/ADJ (1)">
    lovely
   </font>
   <font color="#4E8975" size="1.0" title="temperate/ADJ (1)">
    temperate
   </font>
   <font color="#4E8975" size="1.0" title="rough/ADJ (1)">
    rough
   </font>
   <font color="#4E8975" size="1.0" title="darling/ADJ (1)">
    darling
   </font>
   <font color="#4E8975" size="1.0" title="short/ADJ (1)">
    short
   </font>
   <font color="#00FF00" size="1.0" title="sometimes/ADV (1)">
    sometimes
   </font>
   <font color="#4E8975" size="1.0" title="hot/ADJ (1)">
    hot
   </font>
   <font color="#00FF00" size="1.0" title="often/ADV (1)">
    often
   </font>
   <font color="#4E8975" size="1.0" title="gold/ADJ (1)">
    gold
   </font>
   <font color="#00FF00" size="1.0" title="sometime/ADV (1)">
    sometime
   </font>
   <font color="#4E8975" size="1.0" title="untrimmed/ADJ (1)">
    untrimmed
   </font>
   <font color="#4E8975" size="1.0" title="owest/ADJ (1)">
    owest
   </font>
   <font color="#4E8975" size="1.0" title="wanderest/ADJ (1)">
    wanderest
   </font>
   <font color="#4E8975" size="1.0" title="growest/ADJ (1)">
    growest
   </font>
   <font color="#4E8975" size="1.0" title="mayst/ADJ (1)">
    mayst
   </font>
   <font color="#4E8975" size="1.0" title="yellow/ADJ (1)">
    yellow
   </font>
   <font color="#00FF00" size="1.0" title="where/ADV (1)">
    where
   </font>
   <font color="#4E8975" size="1.0" title="late/ADJ (1)">
    late
   </font>
   <font color="#00FF00" size="1.0" title="away/ADV (1)">
    away
   </font>
   <font color="#4E8975" size="1.0" title="two/ADJ (1)">
    two
   </font>
   <font color="#00FF00" size="1.0" title="whereon/ADV (1)">
    whereon
   </font>
   <font color="#4E8975" size="1.0" title="strong/ADJ (1)">
    strong
   </font>
   <font color="#4E8975" size="1.0" title="true/ADJ (1)">
    true
   </font>
   <font color="#4E8975" size="1.0" title="fixed/ADJ (1)">
    fixed
   </font>
   <font color="#4E8975" size="1.0" title="unknown/ADJ (1)">
    unknown
   </font>
   <font color="#4E8975" size="1.0" title="rosy/ADJ (1)">
    rosy
   </font>
   <font color="#4E8975" size="1.0" title="brief/ADJ (1)">
    brief
   </font>
   <font color="#00FF00" size="1.0" title="why/ADV (1)">
    why
   </font>
   <font color="#4E8975" size="1.0" title="dun/ADJ (1)">
    dun
   </font>
   <font color="#00FF00" size="1.0" title="there/ADV (1)">
    there
   </font>
   <font color="#00FF00" size="1.0" title="well/ADV (1)">
    well
   </font>
   <font color="#4E8975" size="1.0" title="rare/ADJ (1)">
    rare
   </font>
   <font color="#4E8975" size="1.0" title="false/ADJ (1)">
    false
   </font>
  </h1>
  <h1>
   data/whitman
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="alone/ADV (6)">
    alone
   </font>
   <font color="#00FF00" size="80.2" title="so/ADV (5)">
    so
   </font>
   <font color="#00FF00" size="60.400000000000006" title="there/ADV (4)">
    there
   </font>
   <font color="#00FF00" size="40.6" title="yet/ADV (3)">
    yet
   </font>
   <font color="#4E8975" size="40.6" title="one/ADJ (3)">
    one
   </font>
   <font color="#00FF00" size="40.6" title="much/ADV (3)">
    much
   </font>
   <font color="#4E8975" size="40.6" title="free/ADJ (3)">
    free
   </font>
   <font color="#4E8975" size="40.6" title="other/ADJ (3)">
    other
   </font>
   <font color="#00FF00" size="40.6" title="how/ADV (3)">
    how
   </font>
   <font color="#4E8975" size="40.6" title="joyous/ADJ (3)">
    joyous
   </font>
   <font color="#00FF00" size="40.6" title="only/ADV (3)">
    only
   </font>
   <font color="#4E8975" size="20.8" title="swift/ADJ (2)">
    swift
   </font>
   <font color="#4E8975" size="20.8" title="separate/ADJ (2)">
    separate
   </font>
   <font color="#00FF00" size="20.8" title="hardly/ADV (2)">
    hardly
   </font>
   <font color="#00FF00" size="20.8" title="far/ADV (2)">
    far
   </font>
   <font color="#4E8975" size="20.8" title="worthy/ADJ (2)">
    worthy
   </font>
   <font color="#4E8975" size="20.8" title="deep/ADJ (2)">
    deep
   </font>
   <font color="#4E8975" size="20.8" title="dark/ADJ (2)">
    dark
   </font>
   <font color="#4E8975" size="20.8" title="diverse/ADJ (2)">
    diverse
   </font>
   <font color="#4E8975" size="20.8" title="little/ADJ (2)">
    little
   </font>
   <font color="#4E8975" size="20.8" title="dear/ADJ (2)">
    dear
   </font>
   <font color="#4E8975" size="20.8" title="live/ADJ (2)">
    live
   </font>
   <font color="#00FF00" size="20.8" title="near/ADV (2)">
    near
   </font>
   <font color="#4E8975" size="20.8" title="own/ADJ (2)">
    own
   </font>
   <font color="#00FF00" size="1.0" title="vainly/ADV (1)">
    vainly
   </font>
   <font color="#4E8975" size="1.0" title="brave/ADJ (1)">
    brave
   </font>
   <font color="#4E8975" size="1.0" title="immortal/ADJ (1)">
    immortal
   </font>
   <font color="#4E8975" size="1.0" title="deadly/ADJ (1)">
    deadly
   </font>
   <font color="#00FF00" size="1.0" title="ever/ADV (1)">
    ever
   </font>
   <font color="#4E8975" size="1.0" title="proud/ADJ (1)">
    proud
   </font>
   <font color="#00FF00" size="1.0" title="most/ADV (1)">
    most
   </font>
   <font color="#00FF00" size="1.0" title="forth/ADV (1)">
    forth
   </font>
   <font color="#4E8975" size="1.0" title="untold/ADJ (1)">
    untold
   </font>
   <font color="#4E8975" size="1.0" title="mere/ADJ (1)">
    mere
   </font>
   <font color="#00FF00" size="1.0" title="least/ADV (1)">
    least
   </font>
   <font color="#4E8975" size="1.0" title="ecstatic/ADJ (1)">
    ecstatic
   </font>
   <font color="#4E8975" size="1.0" title="simple/ADJ (1)">
    simple
   </font>
   <font color="#4E8975" size="1.0" title="complete/ADJ (1)">
    complete
   </font>
   <font color="#00FF00" size="1.0" title="equally/ADV (1)">
    equally
   </font>
   <font color="#4E8975" size="1.0" title="immense/ADJ (1)">
    immense
   </font>
   <font color="#4E8975" size="1.0" title="furious/ADJ (1)">
    furious
   </font>
   <font color="#4E8975" size="1.0" title="mystic/ADJ (1)">
    mystic
   </font>
   <font color="#4E8975" size="1.0" title="savage/ADJ (1)">
    savage
   </font>
   <font color="#4E8975" size="1.0" title="tender/ADJ (1)">
    tender
   </font>
   <font color="#4E8975" size="1.0" title="bashful/ADJ (1)">
    bashful
   </font>
   <font color="#4E8975" size="1.0" title="feminine/ADJ (1)">
    feminine
   </font>
   <font color="#00FF00" size="1.0" title="thrice/ADV (1)">
    thrice
   </font>
   <font color="#4E8975" size="1.0" title="tied/ADJ (1)">
    tied
   </font>
   <font color="#4E8975" size="1.0" title="untied/ADJ (1)">
    untied
   </font>
   <font color="#4E8975" size="1.0" title="illumin/ADJ (1)">
    illumin
   </font>
   <font color="#00FF00" size="1.0" title="where/ADV (1)">
    where
   </font>
   <font color="#4E8975" size="1.0" title="last/ADJ (1)">
    last
   </font>
   <font color="#4E8975" size="1.0" title="absolv/ADJ (1)">
    absolv
   </font>
   <font color="#4E8975" size="1.0" title="previous/ADJ (1)">
    previous
   </font>
   <font color="#4E8975" size="1.0" title="new/ADJ (1)">
    new
   </font>
   <font color="#4E8975" size="1.0" title="unthought/ADJ (1)">
    unthought
   </font>
   <font color="#4E8975" size="1.0" title="good/ADJ (1)">
    good
   </font>
   <font color="#4E8975" size="1.0" title="sufficient/ADJ (1)">
    sufficient
   </font>
   <font color="#4E8975" size="1.0" title="unprov/ADJ (1)">
    unprov
   </font>
   <font color="#00FF00" size="1.0" title="utterly/ADV (1)">
    utterly
   </font>
   <font color="#4E8975" size="1.0" title="reckless/ADJ (1)">
    reckless
   </font>
   <font color="#4E8975" size="1.0" title="dangerous/ADJ (1)">
    dangerous
   </font>
   <font color="#00FF00" size="1.0" title="thither/ADV (1)">
    thither
   </font>
   <font color="#4E8975" size="1.0" title="brief/ADJ (1)">
    brief
   </font>
   <font color="#00FF00" size="1.0" title="gently/ADV (1)">
    gently
   </font>
   <font color="#00FF00" size="1.0" title="long/ADV (1)">
    long
   </font>
   <font color="#4E8975" size="1.0" title="long/ADJ (1)">
    long
   </font>
   <font color="#00FF00" size="1.0" title="merely/ADV (1)">
    merely
   </font>
   <font color="#00FF00" size="1.0" title="once/ADV (1)">
    once
   </font>
   <font color="#00FF00" size="1.0" title="afterward/ADV (1)">
    afterward
   </font>
   <font color="#00FF00" size="1.0" title="now/ADV (1)">
    now
   </font>
   <font color="#4E8975" size="1.0" title="safe/ADJ (1)">
    safe
   </font>
   <font color="#00FF00" size="1.0" title="too/ADV (1)">
    too
   </font>
   <font color="#4E8975" size="1.0" title="great/ADJ (1)">
    great
   </font>
   <font color="#4E8975" size="1.0" title="perfect/ADJ (1)">
    perfect
   </font>
   <font color="#4E8975" size="1.0" title="irresistible/ADJ (1)">
    irresistible
   </font>
   <font color="#00FF00" size="1.0" title="forever/ADV (1)">
    forever
   </font>
   <font color="#4E8975" size="1.0" title="impatient/ADJ (1)">
    impatient
   </font>
   <font color="#00FF00" size="1.0" title="down/ADV (1)">
    down
   </font>
   <font color="#4E8975" size="1.0" title="green/ADJ (1)">
    green
   </font>
   <font color="#4E8975" size="1.0" title="rude/ADJ (1)">
    rude
   </font>
   <font color="#4E8975" size="1.0" title="unbending/ADJ (1)">
    unbending
   </font>
   <font color="#4E8975" size="1.0" title="lusty/ADJ (1)">
    lusty
   </font>
   <font color="#4E8975" size="1.0" title="certain/ADJ (1)">
    certain
   </font>
   <font color="#00FF00" size="1.0" title="away/ADV (1)">
    away
   </font>
   <font color="#00FF00" size="1.0" title="lately/ADV (1)">
    lately
   </font>
   <font color="#00FF00" size="1.0" title="little/ADV (1)">
    little
   </font>
   <font color="#4E8975" size="1.0" title="else/ADJ (1)">
    else
   </font>
   <font color="#4E8975" size="1.0" title="curious/ADJ (1)">
    curious
   </font>
   <font color="#4E8975" size="1.0" title="manly/ADJ (1)">
    manly
   </font>
   <font color="#4E8975" size="1.0" title="solitary/ADJ (1)">
    solitary
   </font>
   <font color="#4E8975" size="1.0" title="wide/ADJ (1)">
    wide
   </font>
   <font color="#4E8975" size="1.0" title="flat/ADJ (1)">
    flat
   </font>
   <font color="#00FF00" size="1.0" title="very/ADV (1)">
    very
   </font>
   <font color="#00FF00" size="1.0" title="well/ADV (1)">
    well
   </font>
   <font color="#4E8975" size="1.0" title="interminable/ADJ (1)">
    interminable
   </font>
   <font color="#4E8975" size="1.0" title="bright/ADJ (1)">
    bright
   </font>
   <font color="#4E8975" size="1.0" title="frequent/ADJ (1)">
    frequent
   </font>
   <font color="#4E8975" size="1.0" title="continual/ADJ (1)">
    continual
   </font>
   <font color="#00FF00" size="1.0" title="longingly/ADV (1)">
    longingly
   </font>
   <font color="#00FF00" size="1.0" title="somewhere/ADV (1)">
    somewhere
   </font>
   <font color="#00FF00" size="1.0" title="surely/ADV (1)">
    surely
   </font>
   <font color="#4E8975" size="1.0" title="fluid/ADJ (1)">
    fluid
   </font>
   <font color="#4E8975" size="1.0" title="affectionate/ADJ (1)">
    affectionate
   </font>
   <font color="#4E8975" size="1.0" title="chaste/ADJ (1)">
    chaste
   </font>
   <font color="#4E8975" size="1.0" title="matured/ADJ (1)">
    matured
   </font>
   <font color="#00FF00" size="1.0" title="when/ADV (1)">
    when
   </font>
   <font color="#00FF00" size="1.0" title="again/ADV (1)">
    again
   </font>
   <font color="#4E8975" size="1.0" title="able/ADJ (1)">
    able
   </font>
   <font color="#4E8975" size="1.0" title="wealthy/ADJ (1)">
    wealthy
   </font>
   <font color="#4E8975" size="1.0" title="literary/ADJ (1)">
    literary
   </font>
  </h1>
  <h1>
   data/yeats
  </h1>
  <h1>
   <font color="#00FF00" size="100.0" title="when/ADV (11)">
    when
   </font>
   <font color="#00FF00" size="80.2" title="now/ADV (9)">
    now
   </font>
   <font color="#00FF00" size="40.6" title="there/ADV (5)">
    there
   </font>
   <font color="#4E8975" size="30.700000000000003" title="old/ADJ (4)">
    old
   </font>
   <font color="#00FF00" size="30.700000000000003" title="how/ADV (4)">
    how
   </font>
   <font color="#00FF00" size="30.700000000000003" title="never/ADV (4)">
    never
   </font>
   <font color="#00FF00" size="20.8" title="again/ADV (3)">
    again
   </font>
   <font color="#00FF00" size="20.8" title="more/ADV (3)">
    more
   </font>
   <font color="#4E8975" size="20.8" title="young/ADJ (3)">
    young
   </font>
   <font color="#4E8975" size="20.8" title="great/ADJ (3)">
    great
   </font>
   <font color="#00FF00" size="20.8" title="still/ADV (3)">
    still
   </font>
   <font color="#00FF00" size="20.8" title="where/ADV (3)">
    where
   </font>
   <font color="#00FF00" size="20.8" title="so/ADV (3)">
    so
   </font>
   <font color="#00FF00" size="20.8" title="why/ADV (3)">
    why
   </font>
   <font color="#00FF00" size="20.8" title="most/ADV (3)">
    most
   </font>
   <font color="#00FF00" size="10.9" title="somewhere/ADV (2)">
    somewhere
   </font>
   <font color="#4E8975" size="10.9" title="wild/ADJ (2)">
    wild
   </font>
   <font color="#4E8975" size="10.9" title="twilight/ADJ (2)">
    twilight
   </font>
   <font color="#4E8975" size="10.9" title="still/ADJ (2)">
    still
   </font>
   <font color="#4E8975" size="10.9" title="one/ADJ (2)">
    one
   </font>
   <font color="#00FF00" size="10.9" title="well/ADV (2)">
    well
   </font>
   <font color="#00FF00" size="10.9" title="suddenly/ADV (2)">
    suddenly
   </font>
   <font color="#00FF00" size="10.9" title="away/ADV (2)">
    away
   </font>
   <font color="#00FF00" size="10.9" title="once/ADV (2)">
    once
   </font>
   <font color="#00FF00" size="10.9" title="alone/ADV (2)">
    alone
   </font>
   <font color="#4E8975" size="10.9" title="last/ADJ (2)">
    last
   </font>
   <font color="#00FF00" size="10.9" title="whereon/ADV (2)">
    whereon
   </font>
   <font color="#4E8975" size="10.9" title="deep/ADJ (2)">
    deep
   </font>
   <font color="#00FF00" size="10.9" title="always/ADV (2)">
    always
   </font>
   <font color="#4E8975" size="10.9" title="bad/ADJ (2)">
    bad
   </font>
   <font color="#4E8975" size="10.9" title="full/ADJ (2)">
    full
   </font>
   <font color="#4E8975" size="10.9" title="passionate/ADJ (2)">
    passionate
   </font>
   <font color="#00FF00" size="10.9" title="surely/ADV (2)">
    surely
   </font>
   <font color="#00FF00" size="10.9" title="hardly/ADV (2)">
    hardly
   </font>
   <font color="#4E8975" size="10.9" title="slow/ADJ (2)">
    slow
   </font>
   <font color="#4E8975" size="10.9" title="little/ADJ (2)">
    little
   </font>
   <font color="#4E8975" size="10.9" title="proud/ADJ (2)">
    proud
   </font>
   <font color="#4E8975" size="10.9" title="own/ADJ (2)">
    own
   </font>
   <font color="#4E8975" size="10.9" title="high/ADJ (2)">
    high
   </font>
   <font color="#4E8975" size="10.9" title="secret/ADJ (2)">
    secret
   </font>
   <font color="#00FF00" size="1.0" title="above/ADV (1)">
    above
   </font>
   <font color="#4E8975" size="1.0" title="poor/ADJ (1)">
    poor
   </font>
   <font color="#4E8975" size="1.0" title="likely/ADJ (1)">
    likely
   </font>
   <font color="#4E8975" size="1.0" title="happy/ADJ (1)">
    happy
   </font>
   <font color="#00FF00" size="1.0" title="before/ADV (1)">
    before
   </font>
   <font color="#4E8975" size="1.0" title="public/ADJ (1)">
    public
   </font>
   <font color="#4E8975" size="1.0" title="lonely/ADJ (1)">
    lonely
   </font>
   <font color="#4E8975" size="1.0" title="seemed/ADJ (1)">
    seemed
   </font>
   <font color="#00FF00" size="1.0" title="behind/ADV (1)">
    behind
   </font>
   <font color="#4E8975" size="1.0" title="discontented/ADJ (1)">
    discontented
   </font>
   <font color="#4E8975" size="1.0" title="dazzling/ADJ (1)">
    dazzling
   </font>
   <font color="#4E8975" size="1.0" title="indifferent/ADJ (1)">
    indifferent
   </font>
   <font color="#4E8975" size="1.0" title="twere/ADJ (1)">
    twere
   </font>
   <font color="#4E8975" size="1.0" title="living/ADJ (1)">
    living
   </font>
   <font color="#4E8975" size="1.0" title="dry/ADJ (1)">
    dry
   </font>
   <font color="#4E8975" size="1.0" title="nineteen/ADJ (1)">
    nineteen
   </font>
   <font color="#4E8975" size="1.0" title="broken/ADJ (1)">
    broken
   </font>
   <font color="#4E8975" size="1.0" title="clamorous/ADJ (1)">
    clamorous
   </font>
   <font color="#4E8975" size="1.0" title="brilliant/ADJ (1)">
    brilliant
   </font>
   <font color="#4E8975" size="1.0" title="sore/ADJ (1)">
    sore
   </font>
   <font color="#4E8975" size="1.0" title="light/ADJ (1)">
    light
   </font>
   <font color="#4E8975" size="1.0" title="unwearied/ADJ (1)">
    unwearied
   </font>
   <font color="#4E8975" size="1.0" title="cold/ADJ (1)">
    cold
   </font>
   <font color="#4E8975" size="1.0" title="companionable/ADJ (1)">
    companionable
   </font>
   <font color="#4E8975" size="1.0" title="mysterious/ADJ (1)">
    mysterious
   </font>
   <font color="#4E8975" size="1.0" title="beautiful/ADJ (1)">
    beautiful
   </font>
   <font color="#00FF00" size="1.0" title="but/ADV (1)">
    but
   </font>
   <font color="#00FF00" size="1.0" title="even/ADV (1)">
    even
   </font>
   <font color="#4E8975" size="1.0" title="dim/ADJ (1)">
    dim
   </font>
   <font color="#4E8975" size="1.0" title="fallen/ADJ (1)">
    fallen
   </font>
   <font color="#4E8975" size="1.0" title="very/ADJ (1)">
    very
   </font>
   <font color="#00FF00" size="1.0" title="yet/ADV (1)">
    yet
   </font>
   <font color="#4E8975" size="1.0" title="excited/ADJ (1)">
    excited
   </font>
   <font color="#4E8975" size="1.0" title="narrow/ADJ (1)">
    narrow
   </font>
   <font color="#00FF00" size="1.0" title="apart/ADV (1)">
    apart
   </font>
   <font color="#4E8975" size="1.0" title="dimmed/ADJ (1)">
    dimmed
   </font>
   <font color="#00FF00" size="1.0" title="everywhere/ADV (1)">
    everywhere
   </font>
   <font color="#4E8975" size="1.0" title="good/ADJ (1)">
    good
   </font>
   <font color="#4E8975" size="1.0" title="vast/ADJ (1)">
    vast
   </font>
   <font color="#4E8975" size="1.0" title="blank/ADJ (1)">
    blank
   </font>
   <font color="#4E8975" size="1.0" title="pitiless/ADJ (1)">
    pitiless
   </font>
   <font color="#4E8975" size="1.0" title="indignant/ADJ (1)">
    indignant
   </font>
   <font color="#4E8975" size="1.0" title="stony/ADJ (1)">
    stony
   </font>
   <font color="#4E8975" size="1.0" title="rough/ADJ (1)">
    rough
   </font>
   <font color="#00FF00" size="1.0" title="round/ADV (1)">
    round
   </font>
   <font color="#4E8975" size="1.0" title="born/ADJ (1)">
    born
   </font>
   <font color="#4E8975" size="1.0" title="small/ADJ (1)">
    small
   </font>
   <font color="#4E8975" size="1.0" title="loud/ADJ (1)">
    loud
   </font>
   <font color="#4E8975" size="1.0" title="purple/ADJ (1)">
    purple
   </font>
   <font color="#4E8975" size="1.0" title="low/ADJ (1)">
    low
   </font>
   <font color="#4E8975" size="1.0" title="russet/ADJ (1)">
    russet
   </font>
   <font color="#4E8975" size="1.0" title="calm/ADJ (1)">
    calm
   </font>
   <font color="#4E8975" size="1.0" title="lovely/ADJ (1)">
    lovely
   </font>
   <font color="#4E8975" size="1.0" title="brief/ADJ (1)">
    brief
   </font>
   <font color="#4E8975" size="1.0" title="dreamy/ADJ (1)">
    dreamy
   </font>
   <font color="#4E8975" size="1.0" title="kind/ADJ (1)">
    kind
   </font>
   <font color="#00FF00" size="1.0" title="outright/ADV (1)">
    outright
   </font>
   <font color="#4E8975" size="1.0" title="smooth/ADJ (1)">
    smooth
   </font>
   <font color="#4E8975" size="1.0" title="deaf/ADJ (1)">
    deaf
   </font>
   <font color="#4E8975" size="1.0" title="dumb/ADJ (1)">
    dumb
   </font>
   <font color="#4E8975" size="1.0" title="blind/ADJ (1)">
    blind
   </font>
   <font color="#00FF00" size="1.0" title="ever/ADV (1)">
    ever
   </font>
   <font color="#4E8975" size="1.0" title="grey/ADJ (1)">
    grey
   </font>
   <font color="#4E8975" size="1.0" title="easy/ADJ (1)">
    easy
   </font>
   <font color="#4E8975" size="1.0" title="wise/ADJ (1)">
    wise
   </font>
   <font color="#4E8975" size="1.0" title="impossible/ADJ (1)">
    impossible
   </font>
   <font color="#00FF00" size="1.0" title="clearly/ADV (1)">
    clearly
   </font>
   <font color="#00FF00" size="1.0" title="aloud/ADV (1)">
    aloud
   </font>
   <font color="#00FF00" size="1.0" title="here/ADV (1)">
    here
   </font>
   <font color="#4E8975" size="1.0" title="haughty/ADJ (1)">
    haughty
   </font>
   <font color="#4E8975" size="1.0" title="same/ADJ (1)">
    same
   </font>
   <font color="#4E8975" size="1.0" title="wrong/ADJ (1)">
    wrong
   </font>
   <font color="#4E8975" size="1.0" title="dismayed/ADJ (1)">
    dismayed
   </font>
   <font color="#4E8975" size="1.0" title="whole/ADJ (1)">
    whole
   </font>
   <font color="#4E8975" size="1.0" title="noble/ADJ (1)">
    noble
   </font>
   <font color="#4E8975" size="1.0" title="delicate/ADJ (1)">
    delicate
   </font>
   <font color="#4E8975" size="1.0" title="two/ADJ (1)">
    two
   </font>
   <font color="#4E8975" size="1.0" title="troy/ADJ (1)">
    troy
   </font>
   <font color="#00FF00" size="1.0" title="late/ADV (1)">
    late
   </font>
   <font color="#4E8975" size="1.0" title="ignorant/ADJ (1)">
    ignorant
   </font>
   <font color="#4E8975" size="1.0" title="violent/ADJ (1)">
    violent
   </font>
   <font color="#4E8975" size="1.0" title="equal/ADJ (1)">
    equal
   </font>
   <font color="#4E8975" size="1.0" title="peaceful/ADJ (1)">
    peaceful
   </font>
   <font color="#4E8975" size="1.0" title="simple/ADJ (1)">
    simple
   </font>
   <font color="#4E8975" size="1.0" title="tightened/ADJ (1)">
    tightened
   </font>
   <font color="#4E8975" size="1.0" title="natural/ADJ (1)">
    natural
   </font>
   <font color="#4E8975" size="1.0" title="solitary/ADJ (1)">
    solitary
   </font>
   <font color="#4E8975" size="1.0" title="stern/ADJ (1)">
    stern
   </font>
   <font color="#4E8975" size="1.0" title="daring/ADJ (1)">
    daring
   </font>
   <font color="#4E8975" size="1.0" title="different/ADJ (1)">
    different
   </font>
   <font color="#4E8975" size="1.0" title="barbarous/ADJ (1)">
    barbarous
   </font>
   <font color="#00FF00" size="1.0" title="out/ADV (1)">
    out
   </font>
   <font color="#4E8975" size="1.0" title="brazen/ADJ (1)">
    brazen
   </font>
   <font color="#4E8975" size="1.0" title="hard/ADJ (1)">
    hard
   </font>
   <font color="#4E8975" size="1.0" title="mad/ADJ (1)">
    mad
   </font>
   <font color="#4E8975" size="1.0" title="difficult/ADJ (1)">
    difficult
   </font>
  </h1>
 </body>
</html>

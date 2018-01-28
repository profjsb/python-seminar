import nltk
import re
import time
from collections import defaultdict
from configparser import ConfigParser
from gensim import corpora, models, similarities
from nltk.tokenize import RegexpTokenizer
from string import digits


def make_corpus(documents,outdictfile='debate3.dict',mmfile='debate3.mm'):
    
    # Remove documents with less 100 words (some timeline are only composed of URLs)
    documents = [doc for doc in documents if len(doc) > 50]

    # tokenize
    from nltk.tokenize import RegexpTokenizer

    tokenizer = RegexpTokenizer(r'\w+')
    documents = [ tokenizer.tokenize(doc.lower()) for doc in documents ]

    # Remove stop words
    stoplist_tw=['amp','get','got','hey','hmm','hoo','hop','iep','let','ooo','par',
                'pdt','pln','pst','wha','yep','yer','aest','didn','nzdt','via',
                'one','com','new','like','make','top',
                'say','yay','would','going',
                'new','use','should','could','really','see','want',
                'while','know','url','emoji','mention']

    unigrams = [ w for doc in documents for w in doc if len(w)==1]
    bigrams  = [ w for doc in documents for w in doc if len(w)==2]

    stoplist  = set(nltk.corpus.stopwords.words("english") + stoplist_tw
                    + unigrams + bigrams)
    documents = [[token for token in doc if token not in stoplist]
                    for doc in documents]

    # rm numbers only words
    documents = [ [token for token in doc if len(token.strip(digits)) == len(token)]
                    for doc in documents ]

    # Remove words that only occur once
    token_frequency = defaultdict(int)

    # count all token
    for doc in documents:
        for token in doc:
            token_frequency[token] += 1

    # keep words that occur more than once
    documents = [ [token for token in doc if token_frequency[token] > 1]
                    for doc in documents  ]

    # Sort words in documents
    for doc in documents:
        doc.sort()

    # Build a dictionary where for each document each word has its own id
    dictionary = corpora.Dictionary(documents)
    dictionary.compactify()
    # and save the dictionary for future use
    dictionary.save(outdictfile)

    # Build the corpus: vectors with occurence of each word for each document
    # convert tokenized documents to vectors
    corpus = [dictionary.doc2bow(doc) for doc in documents]

    # and save in Market Matrix format
    corpora.MmCorpus.serialize(mmfile, corpus)

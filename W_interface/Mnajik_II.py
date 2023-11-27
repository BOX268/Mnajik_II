"""
29/12/2019

Mnajik: Prototype v2.  Multiple origins and targets.

written w/ python3

Requires supplementary input origin language word list.
Requires extra python3 dependancies, all of which can be downloaded via pip3 install ...

Authors @Gregory Page & @Viktor Martinovic

modified by thibaud michelet :
now use a linguee module instead of google_trans
"""
import LingueeInterface as linguee
import requests
import epitran #https://pypi.org/project/epitran/
from asjp import ipa2asjp
import numpy as np
from similarity.normalized_levenshtein import NormalizedLevenshtein # https://pypi.org/project/strsim/
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import pandas as pd
import pyphen

#functions here

#Distance measures defined here
distance_measure = NormalizedLevenshtein()

def word2asjp(translated_word, destination_langt , destination_lang1):

    # take a translated word
    # ASJP : Automated Similarity Judgment Program
    # return asjp result


    print("\nTranslated word:\n")

    print("\t",translated_word)

    epi = epitran.Epitran(destination_lang1)
    IPA_word = epi.transliterate( translated_word)
    input_ASJP_word = ipa2asjp(IPA_word)


    #print(input_ASJP_word)

    return(input_ASJP_word)

def single_word(words,input_ASJP_word):

    dist = np.array([])

    for i in words[:,2]:

        dist = np.append(dist, [ distance_measure.distance(str(i), input_ASJP_word ) ] )

    #print(  dist[np.argmin(dist)] )

    return(words[np.argmin(dist)])[0] , dist[np.argmin(dist)] #words[np.argmin(dist)])[3] for word-type


def pair_split( words,input_ASJP_word, destination_lang1 ):

    #h = Hyphenator( destination_lang1 )
    # THIS CODE HAS BEEN COMMENTED DUE TO A MODULE CHANGE
    
    # apparently, break down a single word into "syllabes"

    # The new module
    dic = pyphen.Pyphen(lang=destination_lang1)
    asjp_hyphenate = list(dic.iterate(input_ASJP_word))

    out = np.array([])

    for k in range(  len(asjp_hyphenate) ) :

        out1 = np.array([])

        for j in range( len(asjp_hyphenate[k])  ):

            dist = np.array([])

            for i in words[:,2]:

                dist = np.append(dist, [ distance_measure.distance(str(i), asjp_hyphenate[k][j] ) ] )

            #print( dist[np.argmin(dist)] )

            out1 = np.append( out1, ( words[np.argmin(dist)][0], dist[np.argmin(dist)] ) )

        if k == 0:
            out = np.append(out, out1 )
        else:
            out = np.vstack([ out, out1 ] )

    return out


def syllab_split( words, input_ASJP_word, destination_lang1):

    dic = pyphen.Pyphen(lang=destination_lang1)

    asjp_hyphenate = dic.inserted(input_ASJP_word).split("-")

    out = np.array([])

    for j in range( len(asjp_hyphenate)  ):

        dist = np.array([])

        for i in words[:,2]:

            dist = np.append(dist, [ distance_measure.distance(str(i), asjp_hyphenate[j] ) ] )

       # print(words[np.argmin(dist)] , dist[np.argmin(dist)] )

        out = np.append(out, ( words[np.argmin(dist)][0] , dist[np.argmin(dist)] ) )

    return( out )


def vowel_strip_single(words, input_ASJP_word):
    #input asjp word, then strip of vowels
    #read against vowel stripped english word list

    table = str.maketrans(dict.fromkeys('aeiouAEIOU3'))

    dist = np.array([])

    for i in words[:,2]:

        dist = np.append(dist, [ distance_measure.distance(str(i).translate(table), input_ASJP_word.translate(table)) ] )

    return(words[np.argmin(dist)])[0], dist[np.argmin(dist)] #words[np.argmin(dist)])[3] for word-type


def Mnain(input_word, origin, target):

    # intiate the class that will contain the results
    results = Translation()
    results.raw_word = input_word
    #read in word-lists
    # these word lists comes from panda
    if(origin == 0):

        words = pd.read_csv('Wordlists/eng_10000.txt', sep = '\t', header=None).values

    elif(origin == 1):

        words = pd.read_csv('Wordlists/fr_20000.txt', sep = '\t', header=None).values

    elif(origin == 2 ):

        words = pd.read_csv('Wordlists/es_10000.txt', sep = '\t', header=None).values

    elif(origin == 3 ):

        words = pd.read_csv('Wordlists/pt_4926.txt', sep = '\t', header=None).values


    # The purpose of these list is to ling the index of the row chosen and the menu to the language's identifier

    origin_lang_list = ["en", "fr", "es", "pt"]
    #https://py-googletrans.readthedocs.io/en/latest/
    destination_langt_list = ['fr', 'en', 'es', 'it', 'de', 'hu', 'pt']
    destination_langt = destination_langt_list[target]
    #https://pypi.org/project/epitran/?fbclid=IwAR1aCfNbM6weedEgis1Y21XqJifBCqE2102wnaHzmXEn2LjUqy0I7ivBZJo   epitran
    destination_lang1_list = ['fra-Latn', 'eng-Latn', 'spa-Latn', 'ita-Latn', 'deu-Latn', 'hun-Latn', 'por-Latn'] #
    destination_lang1 = destination_lang1_list[target]
    #https://pypi.org/project/PyHyphen/
    destination_lang2_list = ['fr_FR', 'en' ,'es_ES', 'it_IT', 'de', 'hu_HU','pt_BR']
    destination_lang2 = destination_lang2_list[target]
    
    results.originID = origin_lang_list[origin]
    results.targetID = destination_langt_list[target]
    #https://sites.google.com/site/opti365/translate_codes

    linguee_results = linguee.translateSingleWord(input_word, results.originID, results.targetID)
    results.translated_word = linguee_results.translation
    results.examples = linguee_results.examples
    results.ASJP_word = word2asjp(results.translated_word, destination_langt, destination_lang1)
    
    results.pair_split = pair_split(words, results.ASJP_word, destination_lang2)
    
    # change output so it is more readable
    results.success = True
    #result = [translated_word, single_word(words,input_ASJP_word), pair_split( words,input_ASJP_word, destination_lang2 ), syllab_split( words, input_ASJP_word, destination_lang2), vowel_strip_single( words, input_ASJP_word), exampleSentences ]

    return results

class Translation :
    # this class contains all of a translation's results
    
    def __init__(self) :
        self.success = True
        self.errorMsg = ""
        self.raw_word = ""
        self.translated_word = ""
        self.originID = ""
        self.targetID = ""
        
        self.examples = []
        self.ASJP_word = []
        self.pair_split = []
        
    

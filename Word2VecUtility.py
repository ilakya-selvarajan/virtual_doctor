#!/usr/bin/env python
#Ilakya Selvarajan - ML assignment
######## Data cleaning and text processing occurs here! This code is a part of virtual doctor assignment
import re
import nltk

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk.corpus import stopwords


class Word2VecUtility(object):
    

    @staticmethod
    def symptoms_to_wordlist( review, remove_stopwords=True):
        # Function to convert HTML symptoms to a sequence of words,
        # optionally removing stop words.  Returns a list of words.
        #
        # 1. Remove HTML
        review_text = BeautifulSoup(review, "html.parser").get_text(separator=u' ')
        #
        # 2. Remove non-letters
        review_text = re.sub("[^a-zA-Z]"," ", review_text)
        #
        # 3. Convert words to lower case and split them
        words = review_text.lower().split()
        #
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]
        #
        # 4. Return a list of words
        return(words)

    @staticmethod
    def summary_to_wordlist( review):
        # Function to convert HTML summary to a sequence of words,
        # Here, since the summary will be printed out at the end, only beautification will be enough
        #
        # 1. Remove HTML
        review_text = BeautifulSoup(review, "html.parser").get_text(separator=u' ')
        #
        #print review_text 
        return(review_text)

 

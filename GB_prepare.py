import time
import random
from requests import get
from bs4 import BeautifulSoup
import acquire

import pandas as pd
import numpy as np
import unicodedata
import re, os
import json


import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from scipy.stats import zscore




def basic_clean(string):
    
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    string = re.sub(r"[^a-z0-9\s']", '', string).lower()
    
    return string


def tokenize(article:str):
    """ Takes in a string, article, and tokenizes all words """
    
    tokenizer = nltk.tokenize.ToktokTokenizer()

    return tokenizer.tokenize(article, return_str=True)


def stem(article: str):
    """ Takes in a string, article, and returns text after applying stemming using Porter method """
    
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in article.split()]
    article_stemmed = ' '.join(stems)
    
    return article_stemmed



def remove_stopwords(string, extra_words=None, exclude_words=None):
    
    stopword_list = stopwords.words('english')
    
    if exclude_words:
        
        stopword_list = stopword_list + exclude_words
        
    if extra_words:
        
        for word in extra_words:
            
            stopword_list.remove(word)
            
    words = string.split()
    
    filtered_words = [word for word in words if word not in stopword_list]
    
    filtered_string = ' '.join(filtered_words)
    
    return filtered_string


def prepare_df(df):
    """Adds columns for cleaned, stemmed, and lemmatized data in dataframe. 
    Also adds in columns calculating the lengths and word counts. """
    # Create cleaned data column of content
    df['clean'] = df['readme_contents'].apply(basic_clean).apply(tokenize).apply(remove_stopwords)
                                                
    
    # Create stemmed column with stemmed version of cleaned data
    df['stemmed'] = df.clean.apply(tokenize).apply(stem).apply(remove_stopwords)
                                                       

    # Create lemmatized column with lemmatized version of cleaned data
    df['lemmatized'] = df.clean.apply(tokenize).apply(lemmatize).apply(remove_stopwords)
                                                    
    
    # Calculates total length of readme based on number of characters
    df['original_length'] = df['readme_contents'].str.len()
    df['stem_length'] = df.stemmed.str.len()
    df['lem_length'] = df.lemmatized.str.len()

    # Calculates total number of words (splitting up by whitespace)
    df['original_word_count'] = df['readme_contents'].str.split().str.len()
    df['stemmed_word_count'] = df.stemmed.str.split().str.len()
    df['lemmatized_word_count'] = df.lemmatized.str.split().str.len()




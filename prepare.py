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
from sklearn.model_selection import train_test_split



def basic_clean(string):
    
    string = string.lower()
    
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



def remove_stopwords(article: str, extra_words: list, exclude_words: list):
    """ Accepts string (article) as argument and returns text after removing all the stopwords.
    extra_words: any additional stop words to include (these words will be removed from the article)
    exclude_words: any words we do not want to remove. These words are removed from the stopwords list and will remain in article """
    
    stopword_list = stopwords.words('english')

    [stopword_list.append(word_to_add) for word_to_add in extra_words if word_to_add not in stopword_list]
    [stopword_list.remove(to_remove) for to_remove in exclude_words if to_remove in stopword_list]

    words = article.split()
    filtered_words = [w for w in words if w not in stopword_list]

    # print('Removed {} stopwords'.format(len(words) - len(filtered_words)))

    article_without_stopwords = ' '.join(filtered_words)
    
    return article_without_stopwords


def lemmatize(article: str):
    """ Accepts string as argument, article, and returns text after applying lemmatization to each word """
    
    wnl = nltk.stem.WordNetLemmatizer()
        
    lemmas = [wnl.lemmatize(word) for word in article.split()]
    article_lemmatized = ' '.join(lemmas)

    return article_lemmatized



def prepare_df(df, column, extra_words = [], exclude_words = []):
    """Adds columns for cleaned, stemmed, and lemmatized data in dataframe. 
    Also adds in columns calculating the lengths and word counts. """
    # Create cleaned data column of content
    df['clean'] = df[column].apply(basic_clean).apply(tokenize).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)
    
    # Create stemmed column with stemmed version of cleaned data
    df['stemmed'] = df.clean.apply(tokenize).apply(stem).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)

    # Create lemmatized column with lemmatized version of cleaned data
    df['lemmatized'] = df.clean.apply(tokenize).apply(lemmatize).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)
    
    # Calculates total length of readme based on number of characters
    #this is not 100% necessary but it some good extra info to have
    df['original_length'] = df[column].str.len()
    df['stem_length'] = df.stemmed.str.len()
    df['lem_length'] = df.lemmatized.str.len()

    # Calculates total number of words (splitting up by whitespace)
    #this is not 100% necessary but it some good extra info to have 
    df['original_word_count'] = df[column].str.split().str.len()
    df['stemmed_word_count'] = df.stemmed.str.split().str.len()
    df['lemmatized_word_count'] = df.lemmatized.str.split().str.len()

    #this is to do a fill na to the anguages that are nulls
    df['language'] = df.language.fillna(value='No Language')

    #There are two categories Java and javascript I decided to combine the two 
    df = df.replace('Java', 'JavaScript')
    return df

    
def train_validate_test_split(df):
    '''
    This function performs split on github repos data, since there is not enough categories in language we will not stratify.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                   random_state=123)

    return train, validate, test

#This script counts lyric (word) frequency and provides TFIDF analysis on the lyrics 

from nltk.corpus import stopwords 
from collections import Counter
import re 
import numpy as np 
import pandas as pd 
import math 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import fileinput
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Lyrics():
    def __init__(self):
        pass

    def tfidf_scores(self,txt_file):  

        text_file=open(txt_file) 
        lines=text_file.read().split(' , ')
        lines1=' '.join(lines)

        tokenized_sent=sent_tokenize(lines1) #tokenization 
        tokenized_word=word_tokenize(lines1) 
        fdist=FreqDist(tokenized_word) #frequency distribution 

        words1=fdist.keys()
        numbers1=fdist.values() 

        vocab1=list(words1) 
        vocab1=[x.lower() for x in vocab1] #lowercase words 
        symbols='{}()[].,:;+-*/&|<>=~$1234567890?'
        vocab1=[i.translate(symbols).strip() for i in vocab1]
        counts=Counter(vocab1)
        counts.most_common(5)

        #i. clean words 
        vocab2=' '.join(vocab1)
        stripped=re.sub('[^\w\s]','',vocab2)
        stripped=re.sub('__','',stripped)
        stripped1=stripped.split()

        #ii. counting numbers 
        words=word_tokenize(stripped)
        words_counts=Counter(words)
        print(words_counts)

        #iii.tfidf 

        #convert data into a term-frequency matrix 
        cv=CountVectorizer()
        data=cv.fit_transform(stripped1)
        tfidf_transformer=TfidfTransformer()

        #convert term-frequency matrix into tf-idf
        tfidf_matrix=tfidf_transformer.fit(data)

        #create una dictionary to buscando una tfidf para cada palabra 
        word2tfidf=dict(zip(cv.get_feature_names(),tfidf_transformer.idf_))

        for word, score in word2tfidf.items():
            print(word,score)

if __name__=='__main__':
    lyrics=Lyrics()
    lyrics.tfidf_scores('wayne_lyrics.txt')
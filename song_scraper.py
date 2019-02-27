
#This script scrapes lyrics from Metro Lyrics.com 
from bs4 import BeautifulSoup 
import requests
import numpy as np 
import pandas as pd 
import re 
import csv 

class Rap_Artist():
    def __init__(self):
        pass

    def purple_syrup(self,url1):
        #read-in url 
        page1=requests.get(url1)
        soup1=BeautifulSoup(page1.content)

        kush=soup1.find_all('p',class_=re.compile("verse"))
        p = []
        for x in kush:
            p.append(str(kush))

        p1=''.join(p)

        with open("wayne_25.txt", "w") as output: 
            output.write(str(p1))
    
if __name__== '__main__': 
    rap=Rap_Artist()
    rap.purple_syrup("http://www.metrolyrics.com/fireman-lyrics-wayne.htmll")
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:32:55 2019

@author: Khushwant Rai
"""

from bs4 import BeautifulSoup as soup
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer 
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

class book_sum():
    """
    This class assists in scraping a book and simaltaneously genrates the
    summary. The scraping is done on electronic book publication using web
    scrapping techniques. Four types of extractive text summarization techniques 
    have been implemented in _summarize() function. Create object with directory 
    of book as parameter and call book_scrap() function to summarize the book.
    Further, summarized book can be printed using print(object) function.
    """
    def __init__(self,directory='./', book=None):
        self.directory=directory 
        self.book=book
        
    #This function implement 4 types of summarization techniques     
    def _summarize(self, para):
        lex=''
        luhn=''
        lsa=''
        txrank=''        
        parser = PlaintextParser.from_string(para, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        sum0 =summarizer(parser.document,1)
        for sent in sum0:
            lex+=str(sent)

        # #luhn Summarizer  
        # summarizer1 = LuhnSummarizer()
        # sum1 =summarizer1(parser.document,1)
        # for sent in sum1:
        #     luhn+=str(sent)
            
        #  #LSA Summarizer      
        # summarizer2 = LsaSummarizer()
        # sum2 =summarizer2(parser.document,1)
        # for sent in sum2:
        #     lsa+=str(sent)

        # #TextRank Summarizer  
        # summarizer3 = TextRankSummarizer()
        # sum3 =summarizer3(parser.document,1)
        # for sent in sum3:
        #     txrank+=str(sent)
        return lex
    
    #This function get the htm file of every chapter in the book  
    def _get_files(self):
        files=[]
        for filename in os.listdir(self.directory):
            if filename.endswith(".xhtml"): 
                files.append(os.path.join(self.directory, filename))
                continue
            else:
                continue
        return files
  
    #this function scrap the book and simalteneously call summarize() function 
    #to summarize the scraped book
    def book_scrap(self):
        book=[]
        ch=[]
        files=self._get_files()
        for file in files:
            page_soup= soup(open(file,encoding='utf8'),'lxml')
            for j in page_soup.find_all('h1'):
                ch.append(j.text)
            for i in page_soup.find_all('h2'):
                ch.append(i.text)
                for tag in i.next_siblings:
                    if tag!=None and tag!='\n':  
                        s=tag.text.strip()
                        ntemp=s.split(' ')
                        temp=s.split('\n')
                        if len(temp[0].split(' '))<5:
                            t=temp[0]
                            ch.append(t)
                        if len(ntemp)>15:
                            sumry=self._summarize(str(s))
                        ch.append(sumry)               
            book.append(ch)
            ch=[]
        self.book=book
        return book
    
    #this function prints the scrapped and summarized book
    def __str__(self):
        s=''
        for ch in self.book:
            for tp in ch:
                s+=tp+'\n'            
        return s 
        

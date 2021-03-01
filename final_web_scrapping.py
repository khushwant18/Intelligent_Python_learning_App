# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:46:26 2019

@author: vatan
"""
import bs4 as bs
import urllib.request
    
class web_scraping():
    global links
    links=('http://www.allindiaexams.in/engineering/cse/python-mcq/variable-names-operators-data-numeric-types',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/variable-names-operators-data-numeric-types/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/precedence-associativity-bitwise-boolean',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/precedence-associativity-bitwise-boolean/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/formatting-decorators',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/formatting-decorators/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/while-for-loops',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/while-for-loops/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/python-strings',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/python-strings/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/python-strings/3',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/lists-list-comprehension',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/lists-list-comprehension/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/lists-list-comprehension/3',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/tuples-sets',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/tuples-sets/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/dictionary-builtin-functions',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/dictionary-builtin-functions/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/dictionary-builtin-functions/3',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/argument-passing-and-recursion',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/argument-passing-and-recursion/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/mapping-functions-modules',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/mapping-functions-modules/2',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/mapping-functions-modules/3',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/mapping-functions-modules/4',
    # 'http://www.allindiaexams.in/engineering/cse/python-mcq/classes-objects-inheritance-exception-handling',
    'http://www.allindiaexams.in/engineering/cse/python-mcq/classes-objects-inheritance-exception-handling/2')

    def get_soup(self):
        soup_lis=[]
        for i in range(0,len(links)):
            sauce = urllib.request.urlopen(links[i]).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            soup_lis.append(soup)
        return soup_lis
    
    def get_ques(self):
        ques_list=[]
        soup_lis=self.get_soup()
        for soup in soup_lis:
            
            L=[]
            temp=[]
            Ques=[]
            s=''
            l=10000
            for div in soup.find_all('div', class_='qa_list'):
                L.append(div.text)
            for items in L:
                temp=items.split('\n')
                for k in range(len(temp)):
                    temp[k]=temp[k].strip()
                    if temp[k]!='View Answer' and temp[k]!='Workspace' and temp[k]!='Report' and temp[k]!='Discuss' and temp[k]!='Report Error' and temp[k]!='' and temp[k]!='(adsbygoogle = window.adsbygoogle || []).push({});':
                            s+=temp[k]+'\n'
                            if temp[k]=='Explanation:':
                                l=k
                            if k==l+1:
                                Ques.append(s) 
                                s=''                        
            ques_list.append(Ques)                       
        return ques_list
                                
    def get_data(self):
        ques_list=self.get_ques()
        
        data=[]
        for Ques in ques_list:
            collab=[]                                                      
            NQues=[]
            Option=[]
            Answers=[]
            i=0
            for q in Ques:
                for c in range(len(q)):
                    if q[c:c+2]=='A.':
                        NQues.append(q[i:c])
                        k=c
                        i=0
                    if q[c:c+6]=='Answer':
                        Option.append(q[k:c].strip())
                        Answers.append(q[c:len(q)].strip())
                        break
            collab=[NQues,Option,Answers]
            data.append(collab)
        return data
    
    def format_data(self,data):
        ques=[]
        ans=[]
        
        for lv in data:
            for i in range(len(lv[0])):
                ques.append(lv[0][i]+'\n'+lv[1][i])
                ans.append(lv[2][i])
        return ques,ans

obj=web_scraping()

b=obj.get_data()
ques,ans=obj.format_data(b)
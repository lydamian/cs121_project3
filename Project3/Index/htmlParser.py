'''
Created on Nov 15, 2018
 
@author: Kato
'''
import os
from bs4 import BeautifulSoup
from bs4.builder._htmlparser import HTMLPARSER
from nltk.stem.wordnet import WordNetLemmatizer
import json
from fileinput import close
from importlib_metadata._hooks import FileNotFoundError
from nltk.parse.chart import AbstractChartRule
from pymongo import MongoClient
import re
from numpy.lib.utils import _dictlist
 
dirPath= "\\Users\\Kelly\\Documents\\GitHub\\cs121_project3\\WEBPAGES_RAW"
bookeepingPath = "\\Users\\Kelly\\Documents\\GitHub\\cs121_project3\\WEBPAGES_RAW\\bookkeeping.json"
 
class Data():
     
    folderID = -1
    docID = -1
    totalFreq = 0
    headerFreq = 0
    body = 0
    df = 0.0
    tf_idf = 0.0
    url = ""
    strong = 0
    title = 0
    h1 = 0          
    h2 = 0
    h3 = 0 
    h4 = 0
    h5 = 0
    h6 = 0
    def __init__(self, _folderID, _docID):
        self.docID = _docID
        self.folderID = _folderID
 
class WordFrequencyCounter:
    '''
        This is a helper function to check if a term is in a dictionary.
        This function help prevent duplication of terms in the dictionary
    '''
    def isKeyInDictionary(self,dictionary, _key):
        if _key in dictionary:
            return True
        else:
            return False
    def checkDocNumAndFolder(self, dic , docNum, folderNum, term):
        list = dic[term]
        for item in list:
            if(item.folderID == folderNum and docNum == item.docID):
                return item
  
        return None      
         
    def lemmatizer(self, word):
        lmt = WordNetLemmatizer()
        word = lmt.lemmatize(word)
        return word
    def parseString(self, line, dicOfTerm,folderNum,docNum,type1,url):
        '''
            This function parse a string into terms( from project 1). It also keep counts of the term
            frequency where it appear. That's why you see a bunch of if statements.
        '''
        word = ''
        if line is None:
            return
        line += "."
        for char in line:
            if(char.isalnum()):
                if(char.isupper()):
                    char = char.lower()
                word += char
            else:
                if not (word == ''):
                    word = self.lemmatizer(word)
                    if not self.isKeyInDictionary(dicOfTerm, word):
                        key = str(folderNum) + '\\' + str(docNum)
                        data = Data(folderNum,docNum)
                        data.url = url
                        if type1 == "title":
                            data.title = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list})
                        if type1 == "h1":  
                            data.h1 = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "h2":
                            data.h2 = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "h3":
                            data.h3 = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "h4":
                            data.h4 = 1
                            data.totalFreq = 1
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "h5":
                            data.h5 = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list })
                        if type1 == "h6":
                            data.h6 = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "b":
                            data.strong = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "p":
                            data.body = 1
                            data.totalFreq = 1
                            list = []
                            list.append(data)
                            dicOfTerm.update({ str(word): list }) 
                        if type1 == "g":
                            data.totalFreq = 1
                            list1 = []
                            list1.append(data)
                            dicOfTerm.update({ str(word): list1 }) 
                    else:
                        word = self.lemmatizer(word)
                        data = self.checkDocNumAndFolder(dicOfTerm, docNum, folderNum, word) 
                        if ( data == None):
                            data = Data(folderNum,docNum)
                            data.url = url
                            #listOfTerm.append(str(word))
                            if type1 == "title":
                                data.title += 1
                                
                            if type1 == "h1":
                                data.h1 += 1
                                
                            if type1 == "h2":
                                data.h2 += 1
                                
                            if type1 == "h3":
                                data.h3 += 1
                                
                            if type1 == "h4":
                                data.h4 += 1
                                
                            if type1 == "h5":
                                data.h5 += 1
                                
                            if type1 == "h6":
                                data.h6 += 1
                                
                            if type1 == "b":
                                data.strong += 1
                                
                            if type1 == "p":
                                data.body += 1
                                
                            if type1 == "g":
                                data.totalFreq += 1
                            dicOfTerm[word].append(data)
                        else:
                            if type1 == "title":
                                data.title += 1
                            if type1 == "h1":
                                data.h1 += 1
                            if type1 == "h2":
                                data.h2 += 1
                            if type1 == "h3":
                                data.h3 += 1
                            if type1 == "h4":
                                data.h4 += 1
                            if type1 == "h5":
                                data.h5 += 1
                            if type1 == "h6":
                                data.h6 += 1
                            if type1 == "b":
                                data.strong += 1
                            if type1 == "p":
                                data.body += 1
                            if type1 == "g":
                                data.totalFreq += 1
                word=''
 
class htmlParser():
    '''
        THIS FUNCTION IS THE MAIN DRIVER. IT USED OTHER CLASSES AND function to help
        parse html files
         
    '''
    totalFolder = 0
    dicOfTerm = { }
    wordParser = WordFrequencyCounter()
 
    def __init__(self):
        self.totalFolder = self.directorySize(dirPath)
        self.wordParser = WordFrequencyCounter()
        self.dicOfTerm = {}
        self.listOfTerm = []
    def openFile(self, filePath):
        file1 = open(filePath, "r")
        return file1
    def directorySize(self, dirPath):
        # This functions find the size of each folder
        list1 = os.listdir(dirPath)
        number_files = len(list1)
        return number_files
    def readBookKeeping (self):
        # This function find the url in the book 
        with open(bookeepingPath) as data_file:
            data = json.load(data_file)
            return data
    def parseDoc(self, folderNum, docNum):
        # Pass in the folder you want to read
            bookeeping  = self.readBookKeeping()
            folderPath = dirPath + "\\" + str(folderNum )
            size = self.directorySize(folderPath)
 
            docPath =  str(folderPath) + '\\' + str(docNum)
            htmlDoc = self.openFile(docPath)
            soup = BeautifulSoup(htmlDoc,"html.parser")
            for s in soup(["script","style"]):
                s.decompose()
            key = str(folderNum) + '/' + str(docNum)
            url = str(bookeeping.get(key))
            try:
                if not soup.get_text() is None:
                    text = soup.get_text()
                    self.wordParser.parseString(text.strip(),self.dicOfTerm,folderNum,docNum,"g",url)
                #search title
                la = soup.title
                if not soup.title is None:
                    for text in soup.findAll("title"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"title",url)
                #search h1
                if not soup.h1 is None:
                    for text in soup.findAll("h1"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h1", url)
                #search h2
                if not soup.h2 is None:
                    for text in soup.findAll("h2"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h2",url)
                #search h3
                if not soup.h3 is None:
                    for text in soup.findAll("h3"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h3",url)
                #search h4
                if not soup.h4 is None:
                    for text in soup.findAll("h4"):
                        self.wordParser.parseString(text.text.strip(),self.dicOfTerm,folderNum,docNum,"h4",url)
                #search h5
                if not soup.h5 is None:
                    for text in soup.findAll("h5"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h5",url)
                #search h6
                if not soup.h6 is None:
                    for text in soup.findAll("h6"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h6",url)
                #search bold
                if not soup.b is None:
                    for text in soup.findAll("b"):
                        self.wordParser.parseString(  text.text.strip(),self.dicOfTerm,folderNum,docNum,"b", url)
                #search strong
                if not soup.strong is None:
                    for text in soup.findAll("strong"):
                        self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"b", url)
            except:
                #dsfsdfds
                a = 0
            htmlDoc.close()
            return self.dicOfTerm
 
 
def driver():
    p = htmlParser()
    ##inserts lines from file into document inside DB called searchEngine
    client = MongoClient()
    db = client.searchEngine
    dictFile = db.dictFile
      
    docList=[]
      
#     for folderNum in range(0,2): #TODO: change number of folders
#         for docNum in range(0,5): #TODO: change number of docs in folder
#             dic = p.parseDoc(str(folderNum),docNum) #folder number is a string
#      
#             for k,v in dic.items():
#                 for v1 in v:
#                     try:
#                         doc = {
#                         "term": k, 
#                         "folderID": v1.folderID,
#                         "docID": v1.docID,
#                         "tf": v1.totalFreq,
#                         "title": v1.title,
#                         "h1":v1.h1,
#                         "h2":v1.h2,
#                         "h3":v1.h3,
#                         "h4":v1.h4,
#                         "h5":v1.h5,
#                         "h6":v1.h6,
#                         "strong":v1.strong,
#                         "body":v1.body,
#                         "url":v1.url }
#                         docList.append(doc)
#                     except IndexError as ie: print "IndexError:",ie
 
    dic = p.parseDoc("0",2) #folder number is a string
      
    for k,v in dic.items():
        for v1 in v:
            try:
                doc = {
                "term": k, 
                "folderID": v1.folderID,
                "docID": v1.docID,
                "tf": v1.totalFreq,
                "title": v1.title,
                "h1":v1.h1,
                "h2":v1.h2,
                "h3":v1.h3,
                "h4":v1.h4,
                "h5":v1.h5,
                "h6":v1.h6,
                "strong":v1.strong,
                "body":v1.body,
                "url":v1.url }
                docList.append(doc)
            except IndexError as ie: print "IndexError:",ie
              
    result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in docList)]    
      
    for j in result:
        dictFile.insert(j)
        print j['term']
  
driver()


#NEW
 
# '''
# Created on Nov 15, 2018
#  
# @author: Kato
# '''
# import os
# from bs4 import BeautifulSoup
# from bs4.builder._htmlparser import HTMLPARSER
# from nltk.stem.wordnet import WordNetLemmatizer
# import json
# from fileinput import close
# from importlib_metadata._hooks import FileNotFoundError
# from nltk.parse.chart import AbstractChartRule
# from pymongo import MongoClient
# import re
# from numpy.lib.utils import _dictlist
# #Tam
# # dirPath = "\\Users\\Kato\\eclipse-workspace\\SearchEngine\\WEBPAGES_RAW" 
# # bookeepingPath = "\\Users\\Kato\\Downloads\\WEBPAGES_RAW\\bookkeeping.json"
#  
# #Kelly
# dirPath= "\\Users\\Kelly\\Documents\\GitHub\\cs121_project3\\WEBPAGES_RAW"
# bookeepingPath = "\\Users\\Kelly\\Documents\\GitHub\\cs121_project3\\WEBPAGES_RAW\\bookkeeping.json"
#  
# class Data():
#      
#     folderID = -1
#     docID = -1
#     totalFreq = 0
#     headerFreq = 0
#     body = 0
#     df = 0.0
#     tf_idf = 0.0
#     url = ""
#     strong = 0
#     title = 0
#     h1 = 0          
#     h2 = 0
#     h3 = 0 
#     h4 = 0
#     h5 = 0
#     h6 = 0
#     def __init__(self, _folderID, _docID):
#         self.docID = _docID
#         self.folderID = _folderID
#  
# class WordFrequencyCounter:
#     '''
#         This is a helper function to check if a term is in a dictionary.
#         This function help prevent duplication of terms in the dictionary
#     '''
#     def isKeyInDictionary(self,dictionary, _key):
#         if _key in dictionary:
#             return True
#         else:
#             return False
#     def checkDocNumAndFolder(self, dic , docNum, folderNum, term):
#         list = dic[term]
#         for item in list:
#             if(item.folderID == folderNum and docNum == item.docID):
#                 return item
#   
#         return None      
#          
#     def lemmatizer(self, word):
#         lmt = WordNetLemmatizer()
#         word = lmt.lemmatize(word)
#         return word
#     def parseString(self, line, dicOfTerm,folderNum,docNum,type1,url):
#         '''
#             This function parse a string into terms( from project 1). It also keep counts of the term
#             frequency where it appear. That's why you see a bunch of if statements.
#         '''
#         word = ''
#          
#         if line is None:
#             return
#         line += "."
#         for char in line:
#             if(char.isalnum()):
#                 if(char.isupper()):
#                     char = char.lower()
#                 word += char
#             else:
#                 if not (word == ''):
#                     word = self.lemmatizer(word)
#                     if not self.isKeyInDictionary(dicOfTerm, word):
#                         key = str(folderNum) + '\\' + str(docNum)
#                         data = Data(folderNum,docNum)
#                         data.url = url
#                         if type1 == "title":
#                             data.title = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list})
#                         if type1 == "h1":  
#                             data.h1 = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "h2":
#                             data.h2 = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "h3":
#                             data.h3 = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "h4":
#                             data.h4 = 1
#                             data.totalFreq = 1
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "h5":
#                             data.h5 = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list })
#                         if type1 == "h6":
#                             data.h6 = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "b":
#                             data.strong = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "p":
#                             data.body = 1
#                             data.totalFreq = 1
#                             list = []
#                             list.append(data)
#                             dicOfTerm.update({ str(word): list }) 
#                         if type1 == "g":
#                             data.totalFreq = 1
#                             list1 = []
#                             list1.append(data)
#                             dicOfTerm.update({ str(word): list1 }) 
#                          
#                     else:
#                         word = self.lemmatizer(word)
#                         data = self.checkDocNumAndFolder(dicOfTerm, docNum, folderNum, word) 
#                         if ( data == None):
#                             data = Data(folderNum,docNum)
#                             data.url = url
#                             if type1 == "title":
#                                 data.title += 1
#                             if type1 == "h1":
#                                 data.h1 += 1
#                             if type1 == "h2":
#                                 data.h2 += 1
#                             if type1 == "h3":
#                                 data.h3 += 1
#                             if type1 == "h4":
#                                 data.h4 += 1
#                             if type1 == "h5":
#                                 data.h5 += 1
#                             if type1 == "h6":
#                                 data.h6 += 1
#                             if type1 == "b":
#                                 data.strong += 1
#                             if type1 == "p":
#                                 data.body += 1
#                             if type1 == "g":
#                                 data.totalFreq += 1
#                             dicOfTerm[word].append(data)
#                         else:
#                             if type1 == "title":
#                                 data.title += 1
#                             if type1 == "h1":
#                                 data.h1 += 1
#                             if type1 == "h2":
#                                 data.h2 += 1
#                             if type1 == "h3":
#                                 data.h3 += 1
#                             if type1 == "h4":
#                                 data.h4 += 1
#                             if type1 == "h5":
#                                 data.h5 += 1
#                             if type1 == "h6":
#                                 data.h6 += 1
#                             if type1 == "b":
#                                 data.strong += 1
#                             if type1 == "p":
#                                 data.body += 1
#                             if type1 == "g":
#                                 data.totalFreq += 1
#                          
#                 word=''
#  
# class htmlParser():
#     '''
#         THIS FUNCTION IS THE MAIN DRIVER. IT USED OTHER CLASSES AND function to help
#         parse html files
#          
#     '''
#     totalFolder = 0
#     dicOfTerm = { }
#     wordParser = WordFrequencyCounter()
#  
#     def __init__(self):
#         self.totalFolder = self.directorySize(dirPath)
#         self.wordParser = WordFrequencyCounter()
#         self.dicOfTerm = {}
#         self.listOfTerm = []
#     def openFile(self, filePath):
#         file1 = open(filePath, "r")
#         return file1
#     def directorySize(self, dirPath):
#         # This functions find the size of each folder
#         list1 = os.listdir(dirPath)
#         number_files = len(list1)
#         return number_files
#     def readBookKeeping (self):
#         # This function find the url in the book 
#         with open(bookeepingPath) as data_file:
#             data = json.load(data_file)
#             return data
#     def parseDoc(self, folderNum, docNum):
#         # Pass in the folder you want to read
#             bookeeping  = self.readBookKeeping()
#             folderPath = dirPath + "\\" + str(folderNum )
#             size = self.directorySize(folderPath)
#  
#             docPath =  str(folderPath) + '\\' + str(docNum)
#             htmlDoc = self.openFile(docPath)
#             soup = BeautifulSoup(htmlDoc,"html.parser")
#             for s in soup("script", "style"):
#                 s.decompose()
#             key = str(folderNum) + '/' + str(docNum)
#             url = str(bookeeping.get(key))
#             try:
#                 if not soup.get_text() is None:
#                     text = soup.get_text()
#                     self.wordParser.parseString(text.strip(),self.dicOfTerm,folderNum,docNum,"g",url)
#                 #search title
#                 la = soup.title
#                 if not soup.title is None:
#                     for text in soup.findAll("title"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"title",url)
#                 #search h1
#                 if not soup.h1 is None:
#                     for text in soup.findAll("h1"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h1", url)
#                 #search h2
#                 if not soup.h2 is None:
#                     for text in soup.findAll("h2"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h2",url)
#                 #search h3
#                 if not soup.h3 is None:
#                     for text in soup.findAll("h3"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h3",url)
#                 #search h4
#                 if not soup.h4 is None:
#                     for text in soup.findAll("h4"):
#                         self.wordParser.parseString(text.text.strip(),self.dicOfTerm,folderNum,docNum,"h4",url)
#                 #search h5
#                 if not soup.h5 is None:
#                     for text in soup.findAll("h5"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h5",url)
#                 #search h6
#                 if not soup.h6 is None:
#                     for text in soup.findAll("h6"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"h6",url)
#                 #search bold
#                 if not soup.b is None:
#                     for text in soup.findAll("b"):
#                         self.wordParser.parseString(  text.text.strip(),self.dicOfTerm,folderNum,docNum,"b", url)
#                 #search strong
#                 if not soup.strong is None:
#                     for text in soup.findAll("strong"):
#                         self.wordParser.parseString( text.text.strip(),self.dicOfTerm,folderNum,docNum,"b", url)
#             except:
#                 #dsfsdfds
#                 a = 0
#             htmlDoc.close()
#             return self.dicOfTerm
#          
# def driver():
#     p = htmlParser()
#     ##inserts lines from file into document inside DB called searchEngine
#     client = MongoClient()
#     db = client.searchEngine
#     dictFile = db.dictFile
#      
#     #test dictionary
#     print "connection established"
#     dic = p.parseDoc("0",2)
# 
#     docList=[]
#     
#     for k,v in dic.items():
#         for v1 in v:
#             try:
#                 doc = {
#                 "term": k, 
#                 "folderID": v1.folderID,
#                 "docID": v1.docID,
#                 "tf": v1.totalFreq,
#                 "title": v1.title,
#                 "h1":v1.h1,
#                 "h2":v1.h2,
#                 "h3":v1.h3,
#                 "h4":v1.h4,
#                 "h5":v1.h5,
#                 "h6":v1.h6,
#                 "strong":v1.strong,
#                 "body":v1.body,
#                 "url":v1.url }
#                 docList.append(doc)
#             except IndexError as ie: print "IndexError:",ie
#      
#      
# #     for folderNum in range(0,2): #TODO: change number of folders
# #         for docNum in range(0,5): #TODO: change number of docs in folder
# #             dic = p.parseDoc(str(folderNum),docNum) #folder number is a string
# #      
# #             for k,v in dic.items():
# #                 for v1 in v:
# #                     try:
# #                         doc = {
# #                         "term": k, 
# #                         "folderID": v1.folderID,
# #                         "docID": v1.docID,
# #                         "tf": v1.totalFreq,
# #                         "title": v1.title,
# #                         "h1":v1.h1,
# #                         "h2":v1.h2,
# #                         "h3":v1.h3,
# #                         "h4":v1.h4,
# #                         "h5":v1.h5,
# #                         "h6":v1.h6,
# #                         "strong":v1.strong,
# #                         "body":v1.body,
# #                         "url":v1.url }
# #                         docList.append(doc)
# #                     except IndexError as ie: print "IndexError:",ie
#              
#     result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in docList)]    
#      
#     for j in result:
#         dictFile.insert(j)
#         print j['term']
#  
# driver()

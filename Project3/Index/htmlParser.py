'''
Created on Nov 15, 2018

@author: Kato
'''
import os
from bs4 import BeautifulSoup
from bs4.builder._htmlparser import HTMLPARSER
from nltk.stem.wordnet import WordNetLemmatizer
from test.test_decimal import directory
import json
from test.test_socket import try_address
from fileinput import close


dirPath = "/Users/Kato/eclipse-workspace/SearchEngine/WEBPAGES_RAW" 
bookeepingPath = "/Users/Kato/Downloads/WEBPAGES_RAW/bookkeeping.json"

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
        line += "."
        for char in line:
            if(char.isalnum()):
                if(char.isupper()):
                    char = char.lower();
                word += char
            else:
                if not (word == ''):
                    if not self.isKeyInDictionary(dicOfTerm, word):
                        word = self.lemmatizer(word)
                        key = str(folderNum) + '/' + str(docNum)
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
                        
                    else:
                        word = self.lemmatizer(word)
                        data = self.checkDocNumAndFolder(dicOfTerm, docNum, folderNum, word) 
                        if ( data == None):
                            data = Data(folderNum,docNum)
                            data.url = url
                            #listOfTerm.append(str(word))
                            data.totalFreq += 1
                            if type1 == "title":
                                data.title += 1
                                #dicOfTerm[word] = data
                            if type1 == "h1":
                                data.h1 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h2":
                                data.h2 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h3":
                                data.h3 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h4":
                                data.h4 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h5":
                                data.h5 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h6":
                                data.h6 += 1
                                #dicOfTerm[word] = data
                            if type1 == "b":
                                data.strong += 1
                                #dicOfTerm[word] = data
                            if type1 == "p":
                                data.body += 1
                                #dicOfTerm[word] = data
                            
                            dicOfTerm[word].append(data)
                        else:
                            data.totalFreq += 1
                            if type1 == "title":
                                data.title += 1
                                #dicOfTerm[word] = data
                            if type1 == "h1":
                                data.h1 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h2":
                                data.h2 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h3":
                                data.h3 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h4":
                                data.h4 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h5":
                                data.h5 += 1
                                #dicOfTerm[word] = data
                            if type1 == "h6":
                                data.h6 += 1
                                #dicOfTerm[word] = data
                            if type1 == "b":
                                data.strong += 1
                                #dicOfTerm[word] = data
                            if type1 == "p":
                                data.body += 1
                                #dicOfTerm[word] = data
                        
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
            folderPath = dirPath + "/" + str(folderNum )
            docPath =  str(folderPath) + '/' + str(docNum)
            htmlDoc = self.openFile(docPath)
            soup = BeautifulSoup(htmlDoc,"html.parser")
            key = str(folderNum) + '/' + str(docNum)
            url = str(bookeeping.get(key))
            try:
                #search title
                if not soup.title is None:
                    self.wordParser.parseString( str(soup.title.contents),self.dicOfTerm,folderNum,docNum,"title",url)
                #search h1
                if not soup.h1 is None:
                    self.wordParser.parseString( str(soup.h1.contents),self.dicOfTerm,folderNum,docNum,"h1", url)
                #search h2
                if not soup.h2 is None:
                    self.wordParser.parseString( str(soup.h2.contents),self.dicOfTerm,folderNum,docNum,"h2",url)
                #search h3
                if not soup.h3 is None:
                    self.wordParser.parseString( str(soup.h3.contents),self.dicOfTerm,folderNum,docNum,"h3",url)
                #search h4
                if not soup.h4 is None:
                    self.wordParser.parseString( str(soup.h4.contents),self.dicOfTerm,folderNum,docNum,"h4",url)
                #search h5
                if not soup.h5 is None:
                    self.wordParser.parseString( str(soup.h5.contents),self.dicOfTerm,folderNum,docNum,"h5",url)
                #search h6
                if not soup.h6 is None:
                    self.wordParser.parseString( str(soup.h6.contents),self.dicOfTerm,folderNum,docNum,"h6",url)
                #search bold
                if not soup.b is None:
                    self.wordParser.parseString( str(soup.b.contents),self.dicOfTerm,folderNum,docNum,"b", url)
                #search strong
                if not soup.strong is None:
                    self.wordParser.parseString( str(soup.strong.contents),self.dicOfTerm,folderNum,docNum,"b", url)
                #search pa
                if not soup.p is None:
                    self.wordParser.parseString( str(soup.p.contents),self.dicOfTerm,folderNum,docNum,"p",url)
            except:
                a = 0

            htmlDoc.close()
            return self.dicOfTerm


def driver():
    f = open("/Users/Kato/eclipse-workspace/SearchEngine/data.txt", "w")
    p = htmlParser()
    #for folderNum in range(0, self.totalFolder - 2):
    f.write("Term:\t\t\t\tFolder#\tdoc#\tFreq\ttitle\th1\th2\th3\th4\th5\th6\tstrong\tbody")
    for docNum in range(0,20):
        dic = p.parseDoc("0",docNum)
        f.write("\n")
        for k,v in dic.items():
                for v1 in v:  
                    f.write("%s\t\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (k,v1.folderID,v1.docID,v1.totalFreq,v1.title,v1.h1,v1.h2,v1.h3,v1.h4,v1.h5,v1.h6,v1.strong,v1.body))
                    f.write("\n")
        print "Parse doc ", docNum
    f.close()

driver()


'''

p = htmlParser()
file =  p.openFile("/Users/Kato/eclipse-workspace/SearchEngine/data.txt")
soup = BeautifulSoup(file, "html.parser")

print soup.findAll("p")
'''
'''
print soup.title
print soup.h1
print soup.h2
print soup.h3
print soup.h4
print soup.h5
print soup.h6
print soup.b
'''
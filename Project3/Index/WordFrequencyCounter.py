import sys
import operator
import re
import Tkinter
from __builtin__ import True

class WordFrequencyCounter:
    def isKeyInDictionary(self,dictionary, _key):
        if _key in dictionary:
            return True
        else:
            return False
    def parseString(self, line):
        listOfWord = []
        dictOfWord = {}
        word = ''
        for char in line:
            if(char.isalnum()):
                if(char.isupper()):
                    char = char.lower();
                word += char
            else:
                if not (word == ''):
                    if not self.isKeyInDictionary(dictOfWord, word):
                        listOfWord.append(word)
                        dictOfWord.update({word: 1 })
                    else:
                        count = dictOfWord.get(word)
                        count += 1
                        dictOfWord[word] = count

                word=''
                
        return dictOfWord

obj1 = WordFrequencyCounter()



#listOfWord.sort()
#sorted_d = sorted(dictOfWord.items(), key=operator.itemgetter(1), reverse=True)

#for k,v in dictOfWord.items():
    #print(k,v)



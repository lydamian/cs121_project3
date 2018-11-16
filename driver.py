# this is the driver module.
# Tam Hoang
# Damian Ly
# Kelly Tran

import os
import json

class driver:
    
    #TODO: use a database, or just create an index file
    def __init__(self, filename):
        self.filename = filename
        self.collectionList = []
        self.collectionSize = 0
    
        with open(self.filename) as f:
            try:
                data = json.load(f)
            except: print("could not load file")
        for d in data:
            self.collectionList.append(d)
            self.collectionSize = self.collectionSize + 1
            #folder/file, associated url
            print(d, data[d])
        
        for root, dirs, files in os.walk("./WEBPAGES_CLEAN"):
            for name in files:
                doc = os.path.join(root, name)
#                 print(doc)
                # with open(doc, "utf-8") as f2:
                
                
        index = dict()
        
        with open('stopWords.txt', 'r') as f:
            stopWords = [line.strip() for line in f]

    #TODO: tokenize file (use stemming and/or stopWords)
    #inverted index: term, df, docId, tf, tf-idf, url(s), <strong> or <b>, <h1>, <h2>, <h3>, <body>

    #insert terms into dict
    #create inverted index: for each file, for each word, if it's not already in the index, add to {}
    
#     def writeIndexFile(self):


if __name__ == "__main__":
    x = driver("WEBPAGES_CLEAN/bookkeeping.json")
    
#         index = x.createIndex()
#         x.writeIndexFile(...)

    print(x.collectionSize)
    
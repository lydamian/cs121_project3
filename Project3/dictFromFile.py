#to make script: remove def and function call
def dictFromFile():
    dict = {}
    with(open("C:\Users\Kelly\Documents\GitHub\cs121_project3\data.txt","r")) as f:
        for line in f:
            entry = line.split("\t")
            entry = [x for x in entry if x!='' and x!='\n']
#             print entry
            try: 
                key = entry[0]
                entry.pop(0) 
#                 entry.append(object)
                value=entry
#                 print key
#                 print value
                try:
                    dict[key] = value
                except KeyError: pass
            except IndexError: pass
#     test
    try:
        print dict['computer']
        print dict['informatics']
    except KeyError as ke: print "KeyError:", ke
dictFromFile()

##inserts file being written into document into DB called searchEngine
from pymongo import MongoClient
client = MongoClient()
db = client.searchEngine
dictFile = db.dictFile
with (open( ... )) as f2: #open filepaths
    for i in range(0,docNum) #docNum from htmlParser
    #f2.write()
# f2 = open('C:\Users\Kelly\Documents\GitHub\cs121_project3\data.txt')
        dictList= f2.read()
        for line in dictList:
            doc = {
            "term": str(line[0]), # was "data.txt"
            "folderIDslashDocID":str(line[1])+"/"+str(line[2]),
            "tf":line[3],
            "title":line[4],
            "h1":line[5],
            "h2":line[6],
            "h3":line[7],
            "h4":line[8],
            "h5":line[9],
            "h6":line[10],
            "strong":line[11],
            "body":line[12],
            "url":line[13],
            #k,v1.folderID,v1.docID,v1.totalFreq,v1.title,v1.h1,v1.h2,v1.h3,v1.h4,v1.h5,v1.h6,v1.strong,v1.body,v1.url)
#             "list of values" : line[1:] } #takes the tail of the file line, returning the term info list
            dictFile.insert(doc)
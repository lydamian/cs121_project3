
import Tkinter as tk
from Tkinter import StringVar
from pymongo import MongoClient
import json, ast

'''
Database (mongodb) "Schema:
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

'''

# This method calculates tf-idf score for a query
def get_tf_idf():
    print "get_tf_idf_query method called..."
    


# This method computes the cosine_score of a two vectors
# in the vector space model. Most likely this will be 
# A query vector and a document vector pair.
# This method returns top K components of Scores.
def cosine_score(q_vector):
    print "def cosine_score method called.."
    
    '''
    Pseudocode
        float Scores[N] = 0
        float Length[N]
        for each query term t
        do calculate w_t,q and fetch postings list for t
            for each pair(d, tf_td) in postings list
            do Scores[d] += w_t,d * w_t,q
            
        Read the array Length
        for each d 
            do Scores[d] = Scores[d]/Length[d]
            return Top K components of Scores[]
    '''
    


# get value from text box and submit to database
def querySubmitCallback():
    query = E1.get()
    print query

    # connection to database
    try:
        client = MongoClient()
    except:
        print "error connecting to mongodb"
    
    print "Connection Successful"
    
    #Damian
    #db = client.pymongo_test # replace pymongo with database name
    #coll = db.col # replace doc with collection name
    #results = coll.find({'term': query})

    #Kelly
    db = client.searchEngine # replace pymongo with database nam
    dictFile = db.dictFile # replace doc with collection name    
    results = dictFile.find({'term': query})
    
    for doc in results:
        print doc
        print doc['url']
        
    '''
    Summary of Tasks to Complete: 
    1. Represent the query as a weighted tf-idf vector
        - query should be represented as a doc
        - each term in the query will have a tf-idf weight
    2. Represent each document as a weighted tf-idf vector
        - Only retrieve those documents that have at least 1/2 of the query terms?
        - Only retrieve those documents taht have high tf scores?
    3. Compute the cosine similarity score for the query vector
        and each document vector.
    4. Rank documents with resepect to the query by score.
    5. Return the top K (e.g. K = 10) to the user.
    6. Display the top K in the gui? if you got time lol.

    '''
        
    #lemmatize query
    tokenized_query = query.split(" ")
    # - todo please lematize the query tam.
        
    query_weight = get_tf_idf(query)
    
    top_results = cosine_score(query_weight)
    
    #display top_results in the gui format. 
        
    
=======

top = tk.Tk()
top.geometry('250x100')
query = StringVar()
L1 = tk.Label(top, text="SEARCH BAR")
L1.pack( side = tk.TOP)
E1 = tk.Entry(top, textvariable = query, bd = 5)
E1.pack(side = tk.LEFT, fill=tk.X,padx=10)
B1 = tk.Button(top, text="Search", command = querySubmitCallback )
B1.pack(side = tk.RIGHT, fill=tk.X,padx=10)
text = tk.Text(top)
    

    
    
top.mainloop()

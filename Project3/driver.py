
import Tkinter as tk
from Tkinter import StringVar
from pymongo import MongoClient


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




# This method computes the cosine_score of a two vectors
# in the vector space model. Most likely this will be 
# A query vector and a document vector pair.
def cosine_score(q_vector, d_vector):
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
    
    db = client.pymongo_test # replace pymongo with database name
    
    coll = db.col # replace doc with collection name
    
    results = coll.find({'term': query})
    
    for doc in results:
        print doc
        
    '''
    Summary of Tasks to Complete: 
    1. Represent the query as a weighted tf-idf vector
        - query should be represented as a doc
        - each term in the query will have a tf-idf weight
    2. Represent each document as a weighted tf-idf vector
    3. Compute the cosine similarity score for the query vector
        and each document vector.
    4. Rank documents with resepect to the query by score.
    5. Return the top K (e.g. K = 10) to the user.
    6. Display the top K in the gui? if you got time lol.
    '''
        
    
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

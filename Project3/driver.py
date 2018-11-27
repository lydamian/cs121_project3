
import Tkinter as tk
from Tkinter import StringVar
from pymongo import MongoClient
<<<<<<< HEAD
from nltk.stem import WordNetLemmatizer
import math

NUM_DOCUMENT = 37000


class results:
    def __init__(self):
        self.url = ""
        self.cosine_score = 0
        
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
=======
import json, ast
>>>>>>> 72f49b1408e2d4cf921480b0e885a3dd82c36c72

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
# Assuming special case simplification
def get_tf_idf_term(q):
    return 1.0

# This method calculates tf-idf score for a query
# [IN] q - a list of query terms.
# [OUT] returns a floating point value of query weight
# should we assume that each query term has a term freq of one? and
# and we dont need to normalize or multiply by idf as in the notes?
# Lets use special case simplification!
def get_tf_idf_query(q):
    print "get_tf_idf_query method called..."
    weight = 0.0
    for term in q:
        weight += 1.0
        
    print weight
    return weight
    

# This method calculates tf-idf for a document, given q terms.
# [IN] q - a list of query terms
# [IN] d - a row of information in db
# [OUT] return the tf_idf score of document.
def get_tf_idf(t, d):
    print "get_tf_idf_query method called..."
    
    
# This method computes the cosine score of two vectors
# assuming they are not normalized.
def cosine_score(vector1, vector2):
    print "cosine_score called for: " + vector1 + " " + vector2 + "\n"
    return (vector1 * vector2)/(math.sqrt(pow(vector1, 2) + pow(vector2,2)))
    

# This method computes the cosine_score of a two vectors
# in the vector space model. Most likely this will be 
# A query vector and a document vector pair.
# This method returns top K components of Scores.
# [IN] k - maximum number of results to retrieve.
# [IN] q_vector - the query vector (tf-idf)
# [OUT] this method returns top 10 results in a list.
def get_top_results(k, query):
    print "def cosine_score method called.."
    # Local variables
    lemmatizer = WordNetLemmatizer()
    Scores = {} # url, cosine_similarity_score
    Length = {}
    postings_list = None
    
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
    #lemmatize query, remove stop words, remove duplicates, tokenize
    tokenized_query = query.split(" ")
    for term in tokenized_query:
        lemmatizer.lemmatize(term)
        print "token: " + term
        
    # connection to database
    try:
        client = MongoClient()
    except:
        print "error connecting to mongodb"
    print "Connection Successful"
    db = client.pymongo_test # replace pymongo with database name
    coll = db.col # replace doc with collection name           
 
    # Compute Scores
    for term in tokenized_query:
        # retrieve postings list for that term and find term weight
        term_weight = get_tf_idf_term(term)
        results = coll.find({'term': term}) 
        for doc in results:
            weight_of_doc = get_tf_idf(term, doc)
            Scores[doc['url']] += cosine_score(term_weight, weight_of_doc)

    # Return top K scores
    


# get value from text box and submit to database
def querySubmitCallback():
    # local variables
    query = E1.get()
    print query
    
    '''
    # connection to database
    try:
        client = MongoClient()
    except:
        print "error connecting to mongodb" 
    print "Connection Successful"
<<<<<<< HEAD
    db = client.pymongo_test # replace pymongo with database name
    coll = db.col # replace doc with collection name
    results = coll.find({'term': query})
    for doc in results:
        print doc
    '''   
    top_results = get_top_results(10, query)
=======
    
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
>>>>>>> 72f49b1408e2d4cf921480b0e885a3dd82c36c72
    
    top_results = ['doc1','doc2','doc3','doc4','doc5','doc6','doc7','doc8','doc9','doc10']
    #display top_results in the gui format. 
    i = 1
    for doc in top_results:
        print doc
        T.insert(tk.END, i + ". " + doc+"\r\n")
        
    
=======

top = tk.Tk()
top.geometry('500x500')
query = StringVar()
L1 = tk.Label(top, text="SEARCH BAR")
L1.pack( side = tk.TOP)
E1 = tk.Entry(top, textvariable = query, bd = 5)
E1.pack(side = tk.LEFT, fill=tk.X,padx=10)
B1 = tk.Button(top, text="Search", command = querySubmitCallback )
B1.pack(side = tk.RIGHT, fill=tk.X,padx=10)
text = tk.Text(top)

T = tk.Text(top, height=15, width=50)
T.pack(side = tk.BOTTOM)



    
    
top.mainloop()

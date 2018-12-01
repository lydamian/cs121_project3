
import Tkinter as tk
from Tkinter import StringVar
from pymongo import MongoClient
from nltk.stem import WordNetLemmatizer
import math
from pip._vendor.html5lib._ihatexml import letter
from nltk.corpus import stopwords
import numpy as np

NUM_DOCUMENT = 37000


class Result:
    def __init__(self):
        self.url = ""
        self.cosine_score = 0
        self.id = ""
        
class Query:
    def __init__(self):
        self.term = ""
        self.frequency = 0
        
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

def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True

# initializes the query class with each term and its frequency, returns a dictionary of query/freq pairs.
def init_query_req_obj(query):
    d = {}
    for t in query:
        if t in d:
            d[t].frequency = d[t].frequency + 1
        else:
            s = Query()
            d[t] = s
            d[t].term = t;
            d[t].frequency = d[t].frequency + 1
            
    #my_list = list(d.values()
    return d

# Assuming special case simplification
def get_tf_idf_term(term, q):
    if(q.get(term) == None):
        print "strange, got a term that doesnt exist in data structure"
        return 1
    
    tf = q.get(term).frequency
    
    return (1+np.log2(tf))

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
# [IN] doc - a document in mongodb database
# [IN] df - the number of documents a term returned or postings list or length
# [OUT] return the tf_idf score of document.
def get_tf_idf(doc, df):
    print "get_tf_idf_query method called..."
    #tf = doc['tf'] # FIX THIS LATER, HOW TO GET TF FROM A DOC?????
    total_weight = 0
    header_weight = 0
    title_weight = 0
    normal_weight = 0
    
    # get counts of each type
    header_weight = doc['h1'] + doc['h2'] + doc['h3'] + doc['h4'] + doc['h5'] + doc['h6'] # FIX THIS
    title_weight = doc['title']
    normal_weight = doc['tf'] - header_weight - title_weight
    
    # convert counts to actual weights
    header_weight = header_weight * 1.10
    title_weight = title_weight * 1.20
    
    # get total weight
    total_weight = header_weight + title_weight + normal_weight
    return total_weight
    
    
    return ((1 + np.log2(total_weight)) * np.log2((NUM_DOCUMENT/df)))
    
    
    
# This method computes the cosine score of two vectors
# assuming they are not normalized.
def convertToList(dic):
    list1 = []
    for k,v in dic.items():
        list1.append(v)
                     
    return list1


def cosine_score(vector1, vector2):
#     print "cosine_score called for: " + vector1 + " " + vector2 + "\n"
    return (vector1 * vector2)/(math.sqrt(pow(vector1, 2) + pow(vector2,2)))
    
# Returns a tokenized word from an untokenized word
def tokenize_word(word):
    tokenized_word = ''
    word = word.lower()
    
    for letter in word:
        if letter.isalnum():
            tokenized_word += letter
        
    return tokenized_word


# This method computes the cosine_score of a two vectors
# in the vector space model. Most likely this will be 
# A query vector and a document vector pair.
# This method returns top K components of Scores.
# [IN] k - maximum number of results to retrieve.
# [IN] q_vector - the query vector (tf-idf)
# [OUT] this method returns top 10 results in a list.
def get_top_results(k, query):
    print "def cosine_score method called.."
    T.delete('1.0', tk.END)
    
    # Local variables
    lemmatizer = WordNetLemmatizer()
    Scores = {} # url, cosine_similarity_score
    Length = {}
    postings_list = None
    stopWords = set(stopwords.words('english'))
    postings_length = 0
    top_k = []

    
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
    new_query = ""
    for t in query:
        new_query = new_query + t.lower()
    query = new_query
    
    #lemmatize query, remove stop words, tokenize
    tokenized_query = query.split(" ")
    filtered_query = []
    final_query = []
    
    #tokenizing
    for term in tokenized_query:
        filtered_query.append(tokenize_word(term))
        
    #lemmatizing
    j = 0
    for term in filtered_query:
        filtered_query[j] = lemmatizer.lemmatize(term)
        j = j+1
        
    # removing stopwords
    for term in filtered_query:
        if term not in stopWords:
            final_query.append(term)
    
    for term in final_query:
        print term + " "
        
    # storing terms inside a dictionary with dictionary
    query_freq_obj = init_query_req_obj(final_query)
    
    '''
    for v in query_freq_obj:
        print " term: " + v.term + " freq: " +  str(v.frequency)
    '''
        
    # connection to database
    try:
        client = MongoClient()
    except:
        print "error connecting to mongodb"
    print "Connection Successful"
#     db = client.pymongo_test # replace pymongo with database name
#     dictFile = db.col # replace doc with collection name           
    
    #Kelly
    db = client.searchEngine
    dictFile = db.dictFile
    
    '''
    one_item = dictFile.find({'term':'computer'})
    one_item = one_item[0]
    print "oneitem is: " + one_item['term']
    return one_item['term']
    '''
    
    # Compute Scores
    for term in tokenized_query:
        print "term is: " + term
        # retrieve postings list for that term and find term weight
        term_weight = get_tf_idf_term(term, query_freq_obj)
        results = dictFile.find({'term': term})  # DOES THIS RETURN A LIST OF DICTIONARIES?
        postings_length = results.count()
        
        for doc in results:
            doc_weight = get_tf_idf(doc, postings_length)
            doc_id = doc['folderID'] + "/" + str(doc['docID'])
            
            # Add cosine score to the Score dictionary
            result_obj = Result()
            result_obj.url = doc['url']
            result_obj.cosine_score = cosine_score(term_weight, doc_weight)
            # If this is a new document then add to dictionary, else just update value.
            if doc_id in Scores:
                Scores[doc_id].cosine_score = Scores[doc_id].cosine_score + result_obj.cosine_score
                Length[doc_id] = Length[doc_id] + 1
            else:
                Scores[doc_id] = result_obj
                Scores[doc_id].id = doc_id
                Length[doc_id] = Length[doc_id] = 1
                

    for k,v in Scores.items():
        Scores[k].cosine_score = Scores[k].cosine_score/Length[k]

    # Return top K scores - sort then return top 10.
    list_score = convertToList(Scores)
    list_score.sort(key=lambda x: x.cosine_score, reverse=True)
    
#     return ['Jack','John','Food','Icecream']
    
    if(is_empty(list_score)):
        return None
    
    i = 0
    k = 10
    
    while( i < k and i < len(list_score)):
        top_k.append(list_score[i])
        i = i + 1
        
    return top_k


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
    db = client.pymongo_test # replace pymongo with database name
    dictFile = db.col # replace doc with collection name
    results = dictFile.find({'term': query})
    for doc in results:
        print doc
    '''   
    top_results = get_top_results(10, query)
    
    #top_results = ['doc1','doc2','doc3','doc4','doc5','doc6','doc7','doc8','doc9','doc10']
    #display top_results in the gui format. 
    i = 1
    if(top_results == None):
        T.insert(tk.END, 'no results returned')
        return
    
    
    for doc in top_results:
        print doc.url + " " + str(doc.cosine_score)
    
    for doc in top_results:
        T.insert(tk.END, str(i) + ". " + "doc_id: " + doc.id + "\r\n  " + " url: " + doc.url + "\r\n")
        i = i+1
        
    
top = tk.Tk()
top.geometry('800x800') # controls the intitial size of gui
query = StringVar()
L1 = tk.Label(top, text="SEARCH BAR") # Search Bar Header Label
L1.pack( side = tk.TOP)
E1 = tk.Entry(top, textvariable = query, bd = 5, width=100) # text-input bar
E1.pack(side = tk.TOP, fill=tk.X, padx=10)
B1 = tk.Button(top, text="Search", command = querySubmitCallback ) # Button
B1.pack(side = tk.TOP,padx=10)
text = tk.Text(top)
Result_Label = tk.Label(top, text="RESULTS")
Result_Label.pack(side=tk.TOP, padx=10, pady=10)
T = tk.Text(top, height=40, width=100)
T.pack(side = tk.TOP)



    
    
top.mainloop()

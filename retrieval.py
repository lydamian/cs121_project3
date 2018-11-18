import os
import json

def user_prompt():
    #TODO: use GUI for input
    query = raw_input("Enter query: ")
    lookup(query)

def lookup(query):
    query = str(query)
    queryWords = query.split()
    
    with open('stopWords.txt', 'r') as f:
        stopWords = [line.strip() for line in f]
    # removes stop words from query
    queryWords = [x for x in queryWords if x not in stopWords]
    
#     for q in queryWords:
#         for each doc in the index with query=term...
#             get doc info : (folder/file), url, 
    #find 
    
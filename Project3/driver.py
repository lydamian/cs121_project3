
import Tkinter as tk
from Tkinter import StringVar
from pymongo import MongoClient
import json, ast


def cosine_score():
    print "def cosine_score method called.."
    


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

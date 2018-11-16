
import Tkinter as tk
from Tkinter import StringVar

# get value from text box and submit to database
def querySubmitCallback():
    print E1.get()
    #use this query to retrieve information in database/rank
    
    #return to the gui a list of top 10 results, with pagination?
    
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

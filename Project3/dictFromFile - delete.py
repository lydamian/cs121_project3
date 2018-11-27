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
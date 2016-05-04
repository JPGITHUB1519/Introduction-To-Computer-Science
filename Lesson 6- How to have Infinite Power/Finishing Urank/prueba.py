pages = {"a" : ["c","b"] ,"b" : ["a", "c","d"], "c": ["a","b"] }


keys = pages.keys()
page = "d"

#comprobate if a page is a inlink
for i in keys :
                    
    if i!= page :
                        
      if page in pages[i] :

      	print i
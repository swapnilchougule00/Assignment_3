def up_low(string):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in string:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
up_low('The quick Brow Fox')

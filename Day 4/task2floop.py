#search for a number x in this tuple using loop
#{1,4,9,16,25,36,49,64,81,100}

tup1 = (1,4,9,16,25,36,49,64,81,100,64)
X = 64
idx = 0        
for el in tup1:
 
    if(el == X):
        print("the element found",idx)
        break
    idx += 1
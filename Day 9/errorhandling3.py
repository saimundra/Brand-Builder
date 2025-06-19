#finally 
#its raises the messsages if either there is an error or not

try:
    print(x) #error
except:
    print("there is an error on variable") #prints error
finally:
    print("there is ana absolute error")# prints error

try:
    print("hello world!!") #no error
except:
    print("there is an error") #doesnts prints
finally:
    print("there may be a error") #prints the correct answer but stills prints the error too

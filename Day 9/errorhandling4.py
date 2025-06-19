#raise an exception
#you can raise or throw an exception if an condition occurs using raise keyword

x = -1
if x<0 :
    raise Exception("sorry there is no numbers below zero")
 
 
#raise type error
x = "hello world"
if not  type(x) is int:
    raise TypeError("only integers are allowed ")


  
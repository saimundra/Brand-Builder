#syntax:
#lamda arguments : expressions

#example 
#add 10 to argument a , and return the result
x = lambda a : a + 10
print(x(5))

#multiply agrument a with argument b and return the result:
x = lambda a,b : a*b
print(x(5,6))

#summarize argument a,b and c and return the result:
x = lambda a,b,c : a+b+c
print(f"the sum is {x(5,6,7)}")

#use that function definition to make a function that makes the double of the number that you give
def myfunc(n):
    return lambda a:n*a
mydoubler = myfunc(2)
print(mydoubler(11))
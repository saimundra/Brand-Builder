#recursion
#function that calls it repeatedly
#loops and recursion are interrelated

def show(n): #recursive function
    if(n == 0):
        return
    print(n)
    show(n-1)


show(5)


#factorial
def fact(n):
    if(n==0 or n==1):
        return 1
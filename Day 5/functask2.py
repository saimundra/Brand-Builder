#write a function to to find the factorial of n(n is the parameter)

def calc_fac(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)

calc_fac(6)

#waf to convert usd to npr

def conv_npr(usd):
    print("the amount is:",usd*138)

conv_npr(500)
    
#create a class to input users number and print multiplication table and factorial

class ABC:
    def __init__(self,num):
        self.num = num 

    def multiply(self):
        for i in range(1,11):
            mul = num1 * i
            print(mul)

    def factorial(self):
        fact = 1
        for i in range(1 ,num1+1):
            fact *= i
        print(fact)


num1 = int(input("enter a number"))

newABCobject = ABC(num1)
newABCobject.factorial()
newABCobject.multiply()
        
try:
    print(x)
except NameError:
    print("the variable isnot defined") #it prints if there is an error for namerrror
except:
    print("there is an error") #prints errors for others errors than nameerror
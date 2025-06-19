#else
#the else keyword is used when there is no error and the block of code is ready to be executed

try:
    print("hello world")
except NameError:
    print("there's some error in the variable")
else:
    print("everything is all okay and ready to go")

    #in this code try block doesnt have any errors so its prints from the else block
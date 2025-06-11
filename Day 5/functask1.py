#to print the length of the list (list is the parameter)
list1 = [1,2,3,4,5,6,7,8,9,10,11,23,45,67,89,12334]
list2 = [2,3,45,6,7,8,8,99,9,9,0,00,0]
list3 = [2,3,34,4,55,5,67,7,88,9,99,0,00]
list4 = [2,3,4,5,56,6,77,78888,8888,888]
def my_function(list):
    print(len(list))

my_function(list1) #call the function to print the length of list1
my_function(list2)
my_function(list3)
my_function(list4)

#to print the elements of a list in a single line (list is the parameter)
heros = ["superman","spiderman","batman","hulk"]
def func(list):
    print(list)

func(heros[0]) #called the function to print the string at index 0


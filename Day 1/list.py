#list are mutable
list1 = ["apple", "banana", "mango"]
list2 = [ 1, 2, 3]
list3 = [True, False, False]
print(type(list1))
print(list1 ,list2, list3)


list1[0]=("orange") #change gareko
print(list1)
print(type(list1[2]))

print(len(list1[0])) #length
print(list1[1:3]) #slicing
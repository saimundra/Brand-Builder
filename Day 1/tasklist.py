# create a list 2,4,6,8,10 and add prime number 
list1 = [2, 4, 6, 8, 10]
list1.extend([2, 5, 7])
list1.sort()
list1.reverse()
list1.remove(2)
list1.sort(reverse=True)
print(list1)
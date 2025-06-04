list1 = [1, 7, 3,9, 4, 5]
list2 = [1, 2, 3, 4, 5]
list1.append(6) #last ma add garxa append le
print(list1)

list2.extend([6,6,6]) #extend le chai euta list ma multiple kura haru add garnu milxa
print(list2)

list1.sort() #sort in ascending
print(list1)

list1.reverse() #sort in reverse (ulto garney)
print(list1)

list1.sort(reverse= True) #sort in descending
print(list1)

list1.insert(2,5) #list ma kunai pani number add garnu paryo vaney #2= indexing #5= value that you wanna change
print(list1)
list1.insert(3,5)
print(list1)

list1.remove(5) #first ma vako 5 hatyo
print(list1)

list1.pop(4) #tyo index ma vako kura delete gardinxa
print(list1)
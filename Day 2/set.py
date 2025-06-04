#sets --> mutable
#sets elements --> immutable

set1 = {1, 2, 3,4}
set1.add(5) #to add element in a set
print(set1)

set1.remove(2) #to remove an element in a set
print(set1)

set1.clear() #to clear all the elements from the set
print(set1)
print(type(set1))

set2 = {1, 2, 3, 4, 5, 6}
set3 = {4, 5, 6, 7, 8}

#union of the sets
set_union = set2.union(set3)
print(set_union)
 
 #intersection of section
set_intersection = set2.intersection(set3)
print(set_intersection)



#create a set and perform union and intersection
set1 = {"a","b", "c", "d", "e","f"}
set2 ={"e", "f","g","h","i"}
set_union = set1.union(set2)
print(set_union)

set_intersection = set2.intersection(set2)
print(set_intersection)

#complement
setcomp = set2.difference(set1)
print(setcomp)
#dictionary
#dictionary ma key ra value hunxa
#dictionary- unordered, mutable, doesnot support multiple keys

dict1 = {
    "name" : "saimundra", #supports string
    "gpa" : 4, #supports int
    "marks" : [49, 50, 51] #supports list
    

    }

print(dict1)

dict2 = {} #null dictionary paxi future ma chainxa vanera rakhney ho

print(dict1.keys()) #to know the keys of dictionary

print(dict1.values()) #to know the values of the dictionary

print(dict1.get('name')) #to know the values of key

dict1.update({"address" : "pokhara"}) #to add value to the dictionary
print(dict1)


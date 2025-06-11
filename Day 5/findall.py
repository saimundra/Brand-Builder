#findall is a function that matches the pattern and gives us a list of matching characters

import re
pattern = "ai"
txt = "The rain in spain"
match = re.findall(pattern,txt) #match is just an object
print(match)

#if there are no matches an empty list is returned

import re
pattern = "portugal"
txt = "The rain in spain"
match = re.findall(pattern,txt) #an empty list is returned
print(match)


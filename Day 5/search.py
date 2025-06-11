#The search() function searches the string for a match, and returns a Match object if there is a match.

#If there is more than one match, only the first occurrence of the match will be returned:

import re
pattern = "/s"
txt = "the rain in spain"
x = re.search(pattern,txt)
print("the position of the string in white space is: ",x) #nothing found: none
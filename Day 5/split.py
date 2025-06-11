#The split() function returns a list where the string has been split at each match

import re
pattern = "a"
txt = "the rain in spain"
match = re.split(pattern,txt,) #splits a from the list and returns it
print(match)
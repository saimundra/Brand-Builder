#The sub() function replaces the matches with the text of your choice:

import re
pattern ="a"
txt = "the rain in spain"
x = re.sub(pattern,"b",txt) #replaces a by b
print(x)

x= re.sub(pattern, "b",txt, 1) #you can control the number of subs
print(x)
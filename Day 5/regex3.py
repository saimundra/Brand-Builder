import re
pattern ="^The.*Spain$" #starting with The and ending with Rain
txt = "The Rain in Spain"
match = re.search(pattern,txt)
print(match)



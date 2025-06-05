# i = 1
# while i<6:
#     print(i)
#     i += 1

# i =1 
# while i<6:
#     print(i)
#     i += 1

tups1 = (1,4,9,16,25,36,49,64,81,100) #tuple
i = 0
x =36
while i < len(tups1):
    if(tups1[i]==x):
        print("FOUND at idx", i)
    else:
        print("finding..")
    i +=1

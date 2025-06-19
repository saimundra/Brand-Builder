#filehandling
#you can create files,readfiles,updatefiles and delete files using different functions
#open() parameters-filename and mode(types of moses 4)
#read-"r"
#write-"w"
#append-"a"
#create-"x"
#text -"t"
#binary -"b"

f = open("demofile.txt")
print(f.read())

with open ("demofile.txt") as f: #using with statement 
    print(f.read())

#closefiles
f = open("demofile.txt")
print(f.readline()) #reads the first line 
f.close()

with open("demofile.txt") as f:
    print(f.read(5)) #returns the first five characters

#read lines
f = open("demofile.txt")
print(f.readline())

#two read two lines 
f = open("demofile.txt")
print(f.readline())
print(f.readline())



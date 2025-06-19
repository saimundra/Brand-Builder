#write to an existing file 
#to write a file you must add aparameter open() function
#"a "-append - will append to the end of the file 
#"w"- write - will overwrite the existing content
with open("demofile.txt","a") as f:
    f.write("the content is interesting  an the file has more content")

#open the file and read after appending
with open("demofile.txt") as f:
    print(f.read())
    f.close()

#overwriting existing content
with open("demofile.txt","w") as f:
    f.write("oops i have deleted the content!!!")
    f.close()

#reading after over writing the content
with open("demofile.txt")as f:
    print(f.read())

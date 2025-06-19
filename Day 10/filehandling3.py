#create a new file 
# "x"-create -will create a file and returns errors if the file already exists
# "a"- append -will create a file if the specified file doesnt exist
# "w"- write -will create a file if the specified file doesnt exist

#create a new file called "myfile.txt"
with open("myfile.txt","x") as f:#"x" or "a" or "w"
    pass
    

    
    
#write something on the new file 
with open("myfile.txt","w") as f: 
    f.write("this is a new file and the file is empty")
    
with open("myfile.txt","rt") as f: #read the new file
    print(f.read())
    
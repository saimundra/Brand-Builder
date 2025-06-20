# file handling
# Ask user if he wants to Append, read, or cancel.
# Make function for writing and reading

# if you can use OOP

def readfile(filename):
    with open("taskfile,txt","r") as f:
        content = f.read()
        print(content)

def writefile(filename,name, age, address):
    with open("taskfile.txt","a")as f:
        f.write(f"{name},{age},{address}")
while True:
    iscontinue = ("Do you want to add your details: (w/r/c)")
    if(iscontinue == "w"):
        name = str(input("enter your name: "))
        age = int(input("enter your age: "))
        address = str(input("enter your address: "))
        writefile("taskfile.txt",name,age,address)

    elif(iscontinue == "r"):
            readfile("taskfile.txt")

    
    else:
        exit()

    

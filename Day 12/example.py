# def writefile(filename,name,age,address):
#     with open("example.txt","a") as f:
#         f.write(f"{name},{age},{address}")
# while True:
#     iscontinue = input("do you want to go further more:(y/n) ")
#     if(iscontinue == "y" ):
#         name = str(input("enter your name: "))
#         age = int(input("enter your age: "))
#         address = str(input("enter your address: "))
#         writefile("example.txt",name,age,address)
#     else:
#         exit()
    
def readfile(filename):
    with open("example.txt","r") as f:
        while True:
            content = f.readline()
            if (content == ""):
                break
            else:
                data = content.split(",")
                print("------------------")
                print("name", data[0])
                print("age",data[1])
                print("address",data[2])
                


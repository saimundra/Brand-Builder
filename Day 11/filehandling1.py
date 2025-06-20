def writeFile(fileName, name, age, address):
    with open(fileName,"a") as f:
        f.write(f"\n{name}, {age}, {address}")
        #file is directly closed
while True:
    isContinue = input("\nDo you want to add details:(y/n) ")
    if(isContinue=='y'):
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        address = input("Enter the address: ")
        writeFile('studentData.txt', name, age, address)
    else:
        exit()

#python delete file
#to delete a file you must import a OS module and run its os.remove()function

with open("demofile1.txt","x") as f: #demofile1.txt is created
    pass

import os
os.remove("demofile1.txt") #demofile1.txt is deleted
    
#check the file does exists of not
import os
if os.path.exists("demofile1.txt"):
    os.remove("demofile1.txt")
else:
    print("the file doesnt exixts")

#to delete folder
import os 
os.rmdir("myfolder")
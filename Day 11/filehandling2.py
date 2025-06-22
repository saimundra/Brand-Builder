
#To read data

with open("studentData.txt",'r') as f:
    while True:
        content=f.readline()
        if(content==''):
            break
        else:
            data = content.split(',')
            print('-----------------')
            print('Name',data[0])
            print('Age',data[1])
            print('Address',data[2])
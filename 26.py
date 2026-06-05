#File Handling or File Processing

# name = input("Enter your name: ")
# ptr=open("sanju.txt","w")
# ptr.write(name+"\n")
# ptr.close()

# name = input("Enter your name: ")
# ptr=open("sanju.txt","a")
# ptr.write(name+"\n")
# ptr.close()

#Write a program to open a file and write a 5 name's in the file
# for i in range(5):
#     name=input("enter a name : ")
#     ptr=open("sanju.txt","a")
#     ptr.write(name + "\n")
#     #ptr.close() # it is open the file 5 times and close the file 5 time
# ptr.close() # it is open the once and fill the 5 name and close after the filling 5 names

#read()
# ptr1=open("sanju.txt","r")
# data=ptr1.read()
# print(data)
# ptr1.close()

#read(bytes)
# ptr2=open("sanju.txt","r")
# data=ptr2.read(8)
# print(data)
# ptr2.close()

#readline()
# ptr3=open("sanju.txt","r")
# data=ptr3.readline()
# print(data)
# ptr3.close()

# readlines()
# ptr4=open("sanju.txt","r")
# data=ptr4.readlines() #['CristanoRonaldo\n', 'sanju\n', 'abhi\n', 'rahul\n', 'shashank \n', 'nehru\n']
# print(data)
# ptr4.close()


"""Write Program to display take 10 names from the user store in the file and print 7th name from the file"""
for i in range(10):
    name=input("enter your name : ")
    with open("task.txt","a") as f:
        f.write(name + "\n")

with open("task.txt","r") as f:
    data=f.readlines()
    print(data[6])
    f.close()



#tell() and seek()
#tell() : it will give the current position of the cursor
#seek() : using this seek() method we can move the cursor from one position to another position
# ptr=open("sanju.txt","r")
# pos1=ptr.tell()
# res1=ptr.read(8)
# print(res1) #Cristano
#
# pos2=ptr.tell()
# print(pos2) #8
#
# ptr.seek(8)
# pos3=ptr.tell()
# print(pos3) #8
#
# ptr.seek(0)
# pos4=ptr.tell()
# print(pos4) #0
#
# res2=ptr.read(15)
# print(res2) #CristanoRonaldo
# pos5=ptr.tell()
# print(pos5)
# ptr.close()
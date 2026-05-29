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

# ptr1=open("sanju.txt","r")
# data=ptr1.read()
# print(data)
# ptr1.close()

# ptr2=open("sanju.txt","r")
# data=ptr2.read(8)
# print(data)
# ptr2.close()

# ptr3=open("sanju.txt","r")
# data=ptr3.readline()
# print(data)
# ptr3.close()

ptr4=open("sanju.txt","r")
data=ptr4.readlines()
print(data)
ptr4.close()

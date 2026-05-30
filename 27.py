#binary file ("rb","wb")
ptr=open("car.jpg","rb")
data=ptr.read(1000000)
print(data)
ptr.close()

ptr1=open("newcar.png","wb")
ptr1.write(data)
ptr1.close()

#To read image based on the bytes
ptr=open("car.jpg","rb")
data=ptr.read(1000000) #the image show only small part of image based byte code
print(data)
ptr.close()

ptr1=open("newcar.png","wb")
ptr1.write(data)
ptr1.close()

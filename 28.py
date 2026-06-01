import pickle

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
e1=employee("sanju",21)
f=open("sanju.txt","wb")
pickle.dump(e1,f) #pickling using dump() method
f.close()


class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
f=open("sanju.txt","rb")
e=pickle.load(f) #unpickling using load() method
e.display()
f.close()

# 1. Take a list and perform pickling (serialization)
l = [1, 2, 3, 4, 5]
f1 = open("sanju.txt", "wb")
pickle.dump(l, f1)
f1.close()

# 2. Open the file and perform unpickling (deserialization)
f1 = open("sanju.txt", "rb")
data = pickle.load(f1)  # Load the data into a variable
print(data)            # Display the unpickled list
f1.close()
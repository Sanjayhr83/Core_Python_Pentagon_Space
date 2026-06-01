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

#take a list and do pickling, unpickling

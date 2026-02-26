class Hero:
    def __init__(self):
        self.name="sudeep"
        self.age=51
        self.numOfMovies=54     #camel case(lower-upper-lower)
    def act(self):
        print("Sudeep is good actor")
h=Hero()
print(h.name,h.age,h.numOfMovies)
h.act()
h.age=53    #modifing the variable
print(h.age)

class student:
    def __init__(self,name,age,usn):
        self.name=name
        self.age=age
        self.usn=usn
s1=student("rahul",42,420)
print(s1.name,s1.age,s1.usn)
s2=student("shaky",35,60)
print(s2.name,s2.age,s2.usn)

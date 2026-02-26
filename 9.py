#static method and class method
class Mobile:
    def __init__(self):
        self.name = "nokia"
    def call(self):
        print("mobile is ringing")

    @staticmethod
    def charge():
        print("mobile is charging")

    @classmethod
    def hang(cls):
        print("mobile is hanging")
m1=Mobile()
m1.call()
m1.charge()
m1.hang()
Mobile.charge()
Mobile.hang()

class Calci:
    def operation(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c=Calci()
r1=c.operation(1,2)
print(r1)   #In python default tuple will print
r1,r2,r3,r4=c.operation(5,2)    #it takes single value
print(r1)
print(r2)
print(r3)
print(r4)

#default argument and keyword argument
class demo:
    def disp(self,a=10,b=20,c=30):
        print(a,b,c)
d=demo()
x=11
y=22
z=33
d.disp() #10,20,30
d.disp(x,y,z)   #11,22,33
d.disp(z)   #33,20,30
d.disp(y,z) #22,33,30
d.disp(a=z,b=y,c=x) #33,22,11
d.disp(c=y) #10,20,22

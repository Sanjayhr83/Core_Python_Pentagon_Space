'''
Method : method is a behaviour of a object and it will when it is called

Types of methods:
1.instance method : using (self) keyword
2.static method : using () nothing as a keyword
3.class method  : using (cls) keyword

In instance method their is 4 types :
1.no parameter no return value
2.with parameter no return value
3.no parameter with return value
4.with parameter with return value
'''

#no parameter no return value(activation record)
class Calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self) -> None:
        a=10
        b=20
        c=a+b
        print(c)
c=Calculator()
print(c.color)
print(c.brand)
c.add()

#no parameter with return value
class Calci:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def sum(self):
        a=100
        b=50
        c=a+b
        return c
c1=Calci()
print(c1.color)
print(c1.brand)
res=c1.sum()
print(res)

#with parameter no return value
class Calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def add(self,a,b):
        C= a + b
        print(C)
c2=Calculator()
print(c2.color)
print(c2.brand)
x=30
y=40
c2.add(x,y)

#with parameter with return value
class Calculator:
    def __init__(self):
        self.color="black"
        self.brand="casio"
    def sum(self,a,b):
        c=a+b
        return c
c3=Calculator()
print(c3.color)
print(c3.brand)
w=50
z=60
resu=sum(w,z)
print(resu)
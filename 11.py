#functions(def)
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()

#no parameter no return value
def npnr():
    a=10
    b=20
    c=a+b
    print(c)
npnr()

#no parameter with return value
def npwr():
    d=30
    e=40
    f=d+e
    return f
res=npwr()
print(res)

#with parameter no return value
def wpnr(g,h):
    i=g+h
    print(i)
wpnr(3,4)

#with parameter with return value
def wpwr(j,k):
    l=j+k
    return l
res=wpwr(50,20)
j=100
k=200
res=wpwr(j,k)
print(res)

#invoking function through variable
def fun1():
    print("inside fun1")
def fun2():
    print("inside fun2")
ptr1=fun1()
ptr2=fun2()
print(id(fun1))
print(id(ptr1))

#ASCII values(american standard code for information interchange)
alpha=input("enter a alpha : ") #enter only 65 to 90
res=ord(alpha)
print(res)

num=int(input("enter a number : ")) #enter only 97 to 122
res1=chr(num)
print(res1)

#nested function
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
outer()

def train_model():
    epochs = 5
    def print_epoch():
        print(f"Training for {epochs} epochs")
    print_epoch()
train_model()

#higher order function and first order function
def fun1():
    print("inside func1")
def fun2(ptr):
    print("entering fun2")
    ptr()
    print("leaving fun2")
fun1()
fun2(fun1)

#global variable
a=10
def fun1():
    a=100
    b=200
    print(a,b)
def fun2():
    c=500
    print(a)
    print(c)
fun1()
fun2()

#access and modify global variable
q=50 #gloobal variable
def fun():
    print(q)  #access the global variable
fun()
def fun1():
    global q  # access the global variable using global keyword
    q+=5  #modifing the global variable
    print(q)
fun1()

#access and modify the non-local variable
def outer():
    x = 10
    def inner():
        nonlocal x
        x = x + 5
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()

#lambda function
s=lambda a,b:a*b
res=s(5,7)
print(res)

#LEbB rule(local,enclose,global,built-in scopes)
from math import pi #built-in
#pi=10 #global scope
def outer():
    #pi=15 #enclos scope
    def inner():
        #pi=20  #local scope
        print(pi)
    inner()
outer()

#closure(in nested function calling the inner function outside the outer function or outer function after calling the inner function is called closure)
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    return inner #now we only return the function, not a calling
ref=outer()
print(ref)  #now, ref is a special function it is hold inner function, you print the ref it is show memory address of the ref
ref()   # you call the ref() it show inner function print statement

def course():
    print("the institute is Pentagon Space")
    print("The location is BTM")
    def place():
        print("The course is python full stack")
    return place

ref=course()
ref()
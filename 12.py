#filter(), map(), decorator(A decorator is a function that modifies or extends the behavior of another function without changing its code)

#write a program a collect 5 values from users and store in list
l=[]
i=0
while i<=4:
    num=int(input("enter the number : "))
    l.insert(i,num)
    i+=1
print(l)

print("using for loop")
for i in l:
    print(i)

print("using while loop")
i=0
while i<=4:
    print(l[i])
    i+=1

#filtering
def even(unm):
    if num%2==0:
        return True
    else:
        return False
l=[]
i=0
while i<=4:
    num=int(input("enter the number : "))
    l.insert(i,num)
    i+=1
print(l)

i=0
while i<=4:
    data=l[i]
    choice=even(data)
    if choice==True:
        print(l[i])
    i+=1

#same output using filter built-in function syntax:-(filter(function,list_of_elements))
res=list(filter(even,l))
print(res)

##same output using lambda function
res1=list(filter(lambda num:num%2==0,l))
print(res1)

#map() syntax:-(map(function,list_of_elements))
def add(num):
    return num+10
l=[]
i=0
while i <=4:
    num=int(input("Enter a number:"))
    l.append(num)
    i=i+1
print(l)

res2=list(map(add,l))
print(res2)

res2=list(map(lambda num:num+10,l)) #using lambda function
print(res2)

#decorator : Accessing code from one function to another function and if we want to we can modify it without affecting the main code
def main():
    print("main function")
def outer(ptr):
    print("outer function")
    def inner():
        print("enter inner function")
        ptr()
        print("leaving inner function")
    return inner
ref=outer(main)
ref()

#WAP convert string upper or lower using decorators only
def main():
    str=input("enter the string : ")
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        res=ptr()
        ans=res.upper()
        ans1=res.lower()
        ans2=res.capitalize()
        ans3=res.title()
        print(ans)
        print(ans1)
        print(ans2)
        print(ans3)
        print("leaving inner")
    return inner
ref=outer(main)
ref()


def place():    #Main code
    print("BTM is my location...")

def institute(ptr): #outer function
    print("Pentagon Space is my institute...")
    def course():   #inner function
        print("Course Python full stack is my course...")
        ptr()   #calling main function as a parameter
        print("Afternoon batch")
    return course   #return the inner function and not calling the inner function

ref=institute(place)    #main function pass as a parameter to institute function
ref() #innner function return with function, now ref action as a inner function
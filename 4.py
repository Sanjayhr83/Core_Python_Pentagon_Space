#datatype and variable
a=10
b=10
c=10
d=30
print(id(a))   #id is shows the variable id, the same value shows same id for all variable,but different value different value
print(id(b))
print(id(c))
print(id(d))

#types
x=1 #class int
print(x)
print(type(x))
y=1.234     #class float
print(y)
print(type(y))
z="Rahul"       #class string or str
print(z)
print(type(z))

#input statement
u=input("Enter your number: ")  #In this case python consider input value is string
v=input("Enter your number: ")
print(u+v)

i=int(input("Enter a number:")) #using int is tells to value convert string into integer
j=int(input("Enter another number:"))
k=i+j
print(k)

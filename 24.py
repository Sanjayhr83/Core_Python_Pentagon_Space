#set
s1={10,20,30,40,50,60,70,80,90,100}
print(s1) #{100, 70, 40, 10, 80, 50, 20, 90, 60, 30}

s2={10,20,30,40,10,50,20,80,30} #set not allowed duplicate values
print(s2) #{80, 50, 20, 40, 10, 30}

s3={10,20,30}
print(type(s3)) #<class 'set'>

s4={}
print(type(s4)) #<class 'dict'>

s5={11,22,33,44} #set not support indexing and slicing
print(s5[0]) #errorS
print(s5[1:3]) #error

s={10,20,30,40,50}
for i in s:
    print(i)

for i,j in enumerate(s):
    print(i,j)

#empty set
s6=set()
print(type(s6)) #<class 'set'>
for i in range(5):
    data=int(input("enter a number: "))
    s6.add(data) #to add values into set use add method
print(s6)
s6.update([100,200,300]) #to add more than one value into set use update method
print(s6)
s6.discard(300) #to delete value in set use discard method
print(s6)

#union,intersection,difference
s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
s6=s2.difference(s1)
print(s6)
s7=s1.symmetric_difference(s2)
print(s7)

#superset(parent) and subset(child)
s1={1,2,3,4} #Parent->superset
s2={1,2} #child->subset
print(s1.issubset(s2)) #false
print(s1.issuperset(s2)) #True
print(s2.issuperset(s1)) #False
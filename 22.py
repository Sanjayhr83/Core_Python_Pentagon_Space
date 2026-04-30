#List : list is a container which is used to store the heterogeneous data & the data store into square braces [] and separate with comma(,).
"""
features of list :
1. heterogeneous data
2. mutable data
3. dynamic in nature
4. duplications are allowed
5. follows insertion order
"""
l=[]
i=0
while True:
    num=int(input("enter a number : "))
    l.insert(i,num) #l.insert(index,value)
    i=i+1   #increment
    print("do you want to continue")
    print("press 1 for Yes \n press 2 for No")
    choice = int(input("enter your choice : "))
    if choice==1:
        continue
    else:
        break
print(l)

#nested list
l=[10,20,30,["IB","MH","BUZZ"],40]
print(l)
print(len(l))  #5
print(l[4])    #40
print(l[1])    #20
print(l[3][1]) #MH
print(l[3][2]) #BUZZ

l=[10,20,30,["IB","MH","BUZZ",["XL","M80","RX"],"OT"],40]
print(l)
print(len(l))  #5
print(l[4])    #40
print(l[1])    #20 (1D)
print(l[3][1]) #MH (2D)
print(l[3][2]) #BUZZ (2D)
print(l[3][3][2]) #RX (3D)

#copy methods
"""Shallow Copy : it is affect both object"""
l0=[10,20,30,40,50]
l1=l0   #shallow copy
print(l0)
print(l1)
l0[3]=3000  #modify the object
print(l0)
print(l1)

"""Deep Copy : it is affect only one object"""
l2=[10,20,30,40,50]
l3=l2.copy()
print(l2)
print(l3)
del l2[2]
print(l2)
print(l3)

#nested list
l=[10,20,["MH","IB"],40]
l1=l.copy()
print(l)
print(l1)
l[2][1]="BUZZ"
print(l)
print(l1)

#achieving deep copy in nested list
import copy
l=[10,20,["MH","IB"],40]
l1=copy.deepcopy(l) #deep copy in nested list
print(l)
print(l1)
l[2][1]="BUZZ"
print(l)
print(l1)

#built-in functions in list (len,min,max,type,all,any,sorted)
l=[10,20,30,40,50]
print(l)
print(len(l))
print(min(l))
print(max(l))
print(type(l))

l1=[1,0,1,2]
print(l1)
print(all(l1))
print(any(l1))

l2=[0,0,0,0]
print(l2)
print(all(l2))
print(any(l2))

l3=[0,0,1,0]
print(l3)
print(all(l3))
print(any(l3))

l4=[1,20,"pentagon",30]
print(l4)
print(all(l4))
print(any(l4))

l5=["rahul","rama"]
print(l5)
print(all(l5))
print(any(l5))

l6=[89,78,54,90,74,23]
print(sorted(l6))

#slicing and indexing
l=[10,20,30,40,50,60,70,80,90]
print(l)
print(len(l))
print(l[5])
print(l[7])
print(l[-1])
print(l[-7])
print(l[2:7])
print(l[2:6:2])
print(l[-2:-7])
print(l[-8:5])
print(l[-8:-3])
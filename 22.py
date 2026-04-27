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
#tuple
t1=(10,20,30)
print(t1)
print(type(t1)) #<class 'tuple'>

t2=(10,"ram",20.8)
print(t2)
print(type(t2)) #<class 'tuple'>

t3=(10)
print(t3)
print(type(t3)) #<class 'int'>

t4=(20,)
print(t4)
print(type(t4)) #<class 'tuple'>

#Mutable v/s immnutablee
l=[10,20]
l[0]=50
print(l) #[50,20]

t=(20,30)
t[0]=100 #Error
print(t)

#indexing and slicing
R=(10,20,30,"Manja","Soumya",40)
print(len(R)) #6
print(R[3]) #Manja
print(R[-2]) #Soumya
print(R[1:4]) #[20, 30, 'Manja']
print(R[2:5:2]) #[30, 'Soumya']
print(R[-1:-4:-1]) #[40, 'Soumya', 'Manja']
print(R[::2]) #[10, 30, 'Soumya']
print(R[::-1]) #[40, 'Soumya', 'Manja', 30, 20, 10]

#Special Operators in Tuple
S=(10,20,30,40)
print(10 in S)  #True
print(50 in S) #False
print(100 not in S) #True
print(20 not in S) #False

#Nested Tuple
M=(1,2,3,("A","B","C"),4)
print(len(M)) #5
print(M[1]) #2
print(M[3][1]) #B
print(M[3][2]) #C
print(M[4]) #4

#List within the Tuple
k=("Sanju",[94,92,84]) #packing
name,marks=k    #unpacking
print(name) #Sanju
print(marks) #[94, 92, 84]

#zip_lengest() :-
from itertools import zip_longest
name=["Rohit","kohli","Rahul","dhoni"]
Team_name=["MI","RCB","DC","CSK"]
Trophies=["Five","one"]
res=list((zip_longest(name,Team_name,Trophies)))
print(res) #[('Rohit', 'MI', 'Five'), ('kohli', 'RCB', 'one'), ('Rahul', 'DC', None), ('dhoni', 'CSK', None)]
#dictionary : key and value pair
student={
    "name":"sanju",
    "age":27,
    "gender":"male"
}
print(student)
print(type(student))
student["mob"]=7411
print(student)
student["age"]=21
print(student)

#iterating dictionary
employee={
    "name":"abhi",
    "age":22,
    "gender":"male"
}
print(employee)
for i in employee: #initially i pointing out keys
    print(i) #print only keys
print(employee["name"])
for i in employee:
    print(employee[i])
for i in employee.keys():
    print(i) #only keys
for i in employee.values():
    print(i) #only values
for i in employee.items():
    print(i) #both keys and values in the form of tuple

#nested dictionary
student={
    "name":"shaky",
    "age":35,
    "phone_num":{
        "mob":1001,
        "landline":2002
    },
    "address":{
        "resi":"maldives",
        "permanent":"Pentagon"
    }
}
print(student)
print(student["age"]) #1D
print(student["address"]["resi"]) #2D
print(student["phone_num"]["landline"]) #2D

#Shallow copy and deep copy in dictionary
student={
    "name":"sanju",
    "age":20
}
print(student)
s1=student #shallow copy
s2=student.copy() #deep copy
student["age"]=21
print(student)
print(s1)
print(s2)
print(student)

#achieving the deep copy in nested dictionary
import copy
hero={
    "name":"ram",
    "addr":{
        "res":"kengeri",
        "perm":"BTM"
    }
}
print(hero)
h1=hero.copy() #shallow copy
h2=copy.deepcopy(hero) #deep copy
hero["addr"]["perm"]="Majestic"
print(hero)
print(h1)
print(hero)
print(h2)

#zip() in dictionary
emp_id=[101,102,103,104]
names=["shaky","rahul","rakshith","nehru"]
res=dict(zip(emp_id,names)) #emp_id="keys" & names="values
print(res)
mob=[11,420,840,7]
addr=["pentagon","Thailand","russia","india"]
# info=dict(zip(emp_id,names,mob,addr)) #error because interpreter confuse to take which one is key which one value
# print(info)
res1=list(zip(names,mob,addr))
final_info=dict(zip(emp_id,res1))
print(final_info)
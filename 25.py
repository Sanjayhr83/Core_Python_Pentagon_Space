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
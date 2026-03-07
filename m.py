def fun():
    print("function1")
def fun1():
    print("function2")


#find duplicate value and remove duplicate value
l=[1,2,3,4,5,3,4,6,7,3,9,7,8,9,7]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i],"is duplication")
            break
print(list(set(l)))
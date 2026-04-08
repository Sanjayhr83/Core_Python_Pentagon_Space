#Exception Handling
a=int(input("enter a value : "))
b=int(input("enter a value : "))
try:
    res=a/b
    print(res)
except Exception as e:
    print("Error is",e)

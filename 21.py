#Exception Handling
"""
try : Risk code written in this block
except: To know the error is occurring
else : it this run when except block not show error
finally: it is run always end to the execution code block
"""
a=int(input("enter a value : "))
b=int(input("enter a value : "))
try:
    res=a/b
    print(res)
except Exception as e:
    print("Error is",e)

def fun1():
    print("entering function1")
    try :
        fun2()
    except Exception as e:
        print("Error is",e)
    print("leaving function1")

def fun2():
    print("entering function2")
    res=10/0
    print(res)
    print("leaving function2")
print("program start")
fun1()
print("program end")
#Exception Handling
"""
try : Risk code written in this block
except: To know the error is occurring
else : it this run when except block not show error
finally: it is run always end to the execution code block
raise : allows you to force an error to occur
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
        fun2()  # if error occur here then go to except block
    except Exception as e:
        print("Error is",e)
    print("leaving function1")

def fun2():
    print("entering function2")
    res=10/0    # in this line error will occur and go & hit to PVM, enter to except block show which type of error and PVM create superate block of memory with address
    print(res)
    print("leaving function2")
print("program start")
fun1()
print("program end")

def ps():
    print("Starting internship....")
    try:
        course()  # if error occur here then go to except block
    except Exception as e:
        print(f"Error: {e}")
    print("Internship completed....")


def course():
    print("...Course is Python full stack...")
    res = 10 / 0  # in this line error will occur and go & hit to PVM, enter to except block show which type of error and PVM create superate block of memory with address
    print(res)
    print("Fees is free because CSR Drive")

print("Ending of 7th Semester")
ps()
print("Ending of Engineering")

#Rethrough error in Exceptional handling (using raise keyword)
def fun1():
    print("entering function1")
    try :
        fun2()  # if error occur here then go to except block
    except Exception as e:
        print("Error is",e)
    print("leaving function1")

def fun2():
    print("entering function2")
    try :
        res=10/0
        print(res)
    except Exception as e:
        print("Error is",e)
        raise e
    print("leaving function2")
print("Program start")
fun1()
print("Program end")


#finally block
def fun1():
    print("entering function1")
    try :
        fun2()  # if error occur here then go to except block
    except Exception as e:
        print("Error is",e)
    print("leaving function1")

def fun2():
    print("entering function2")
    try :
        res=10/0
        print(res)
    except Exception as e:
        print("Error is",e)
        raise e
    finally:
        print("leaving function2")
print("Program start")
fun1()
print("Program end")

def movie1():
    print("Movie starting")
    try:
        movie2()
    except Exception as e:
        print("sound is not hearing")
    print("Movie ending")

def movie2():
    print("second Movie starting")
    try:
        t=15/0
        print(t)
    except Exception as e:
        print("movie is very bad")
        raise e
    finally:
        print("Second Movie ending")
print("Ticket conform")
movie1()
print("Day completed")

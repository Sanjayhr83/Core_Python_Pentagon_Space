#Condition statements(if,elif,else)

'''
there is no do-while loop and switch case in python ,but match case in python it is support only python 3.10+ versions
'''

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

#Practice ex(Bus ticket)
print(".......WELCOME TO MY BUS!!......")
a=input("Enter a gender or status: ")
b=int(input("Enter age: "))
if a=="male" and b>=7:
    print("Pay full charge")
elif a=="female" and b>=1:
    print("Free of cost")
elif a=="female" and b>=60:
    print("Free of cost + Senior citizens(use any option)")
elif a=="male" and b>=60:
    print("Senior citizen")
elif a=="student"and b<25:
    print("Student Pass")
else:
    print("Please enter valid input")

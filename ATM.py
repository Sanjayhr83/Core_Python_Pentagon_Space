while True:
    import time
    c_pin=1234
    balance=5000
    print("...welcome to ATM...")
    print("insert atm card")
    print("choice 1.insert successfully\n2.insert card properly")
    choice=input("enter your choice : ")

    if choice=="1":
        print("insert successfully")
        p=int(input("enter your pin : "))
        if p==c_pin:
            print("your pin is correct")
            print("select language\n1.English\n2.kannada\n3.hindi")
            lang = input("enter your choice: ")
            if lang == "1":
                print("select english")
                print("select\n1.balance querying\n2.withdraw cash")
                b=input("enter your choice: ")
                if b=="1":
                    time.sleep(3)
                    print("your balance is", balance)
                    print("thank you for using ATM")
                elif b=="2":
                    w=int(input("enter your withdraw cash :"))
                    time.sleep(3)
                    print(balance-w)
                    print("thank you for using ATM")
                else:
                    print("please enter correct choice")
                    break
            else:
                print("please enter correct choice")
                break
        else:
            print("please enter correct choice")
            break
    elif choice=="2":
        print("please take return your card and insert properly")
        break
    else:
        print("please enter correct choice")


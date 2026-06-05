# Multitasking or Multi-Processing
"""the ability to do a multiple simultaneously is called multitasking"""
# Single Threading
import time
class demo:
    def printname(self):
        l=["sanjay","rajappa","shashank"]
        for i in l:
            print(i)
            time.sleep(3)
    def printnumber(self):
        for i in range(10):
            print(i)
            time.sleep(3)
    def add(self):
        a=10
        b=20
        c=a+b
        print(f"{a}+{b}={c}")
d1=demo()
d1.printname()
d1.printnumber()
d1.add()


from threading import Thread
class Data(Thread):
    def run(self):
        for i in range(11):
            # Added flush=True so the output prints immediately without waiting for a newline
            print(i, end=" ", flush=True)
            time.sleep(0.9)
class Checkout(Thread):
    def run(self):
        print("\n[Names starting]")
        l = ["vasant", "vassim", "chethan", "surya"]
        for i in l:
            print(f"\nName: {i}")
            time.sleep(1)
class Flim(Thread):
    def run(self):
        print("\n[Movie starting]")
        m = ("kgf", "robert", "kalki", "yuva", "arasu")
        for j in m:
            print(f"\nMovie: {j}")
            time.sleep(0.8)
# Object creation
d1 = Data()
c1 = Checkout()
f1 = Flim()
# Starting threads (this will now correctly look for the run() method)
d1.start()
c1.start()
f1.start()
# Good practice: Wait for all threads to finish before exiting the script
d1.join()
c1.join()
f1.join()

#Multi-Threading
import time
from threading import Thread
class Task(Thread):
    def run(self):
        l = ["sanjay", "rajappa", "shashank"]
        for i in l:
            print(i)
            time.sleep(3)
class Task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(3)
class Task3(Thread):
    def run(self):
        a=10
        b=20
        c=a+b
        print(f"{a}+{b}={c}")
t1=Task()
t2=Task2()
t3=Task3()
t1.start()
t2.start()
t3.start()



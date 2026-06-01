# Multi-tasking or Multi-Processing
"""the ability to do a multiple simultaneously is called multi-tasking"""

# Single Therading
# import time
# class demo:
#     def printname(self):
#         l=["sanjay","rajappa","shashank"]
#         for i in l:
#             print(i)
#             time.sleep(3)
#     def printnumber(self):
#         for i in range(10):
#             print(i)
#             time.sleep(3)
#     def add(self):
#         a=10
#         b=20
#         c=a+b
#         print(f"{a}+{b}={c}")
# d1=demo()
# d1.printname()
# d1.printnumber()
# d1.add()

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



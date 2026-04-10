#looping statement(for,while)
# for loop
for i in 1, 2, 3, 4:
    print(i)
for i in 1, 2, "rahul", 3:
    print(i)
for i in "rahul", "ramya":
    print(i)
for i in "rahul":
    print(i)
#printing tables using for loop
for i in range(1,11):
    print(f"2 X {i} = {i*2}")

#range function(start,stop,step)
for i in range(100):
    print(i)
for i in range(1, 100):
    print(i)
for i in range(1, 100, 2):  #print only print even number
    print(i)
for i in range(2, 100, 2):  #print only odd number
    print(i)

# while loop (initialization,condition,increment or decrement all are mandatory)
i = 0  #initialize
while i <= 2:  #condition
    print("hello")
    i += 1  #increment

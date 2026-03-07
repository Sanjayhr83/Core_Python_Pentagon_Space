#generator
def generator():
    yield 1
    yield 2
    yield 3
res=generator()
print(next(res))
print(next(res))
print(next(res))
print(res)
print(next(res))#stop iteration error because their is no next line

#Using Generator with Loop
def numbers():
    for i in range(5):
        yield i
for num in numbers():
    print(num)


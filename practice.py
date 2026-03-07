def number():
    for i in range(5):
        yield i
for num in number():
    print(num)

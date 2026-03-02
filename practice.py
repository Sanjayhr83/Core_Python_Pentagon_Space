def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    return inner
ref=outer()
print(ref)
ref()
#decorator
def main():
    print("main function")
def outer(ptr):
    print("outer function")
    def inner():
        print("enter inner function")
        ptr()
        print("leaving inner function")
    return inner
ref=outer(main)
ref()
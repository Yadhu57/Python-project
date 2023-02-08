def outer(func):
    def inner():
        print("I got Decorated")
        func()
        return inner
@outer
def ordinary():
    print("I an ordinary")

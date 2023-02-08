class cls:
    def fn(self, name=None):
        if name is None:
            print("Hello")
        else:
            print("Hello " + name)


obj = cls()
obj.fn()
obj.fn("Yadhu")

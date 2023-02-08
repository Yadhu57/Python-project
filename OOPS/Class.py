class Cls:
    a = 10

    def fun(self):
        print("Function inside the class")


obj = Cls()
obj.fun()
print("value of a inside the class=", obj.a)

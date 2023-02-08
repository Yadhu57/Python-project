def upper_decor(fun):
    def wrapper(name):
        result = fun(name)
        return result.upper()

    return wrapper


@upper_decor                 # decorator
def hello_name(name):
    return "hello " + name

# f = upper_decor(hello_name)            #using instead of decorator
print(hello_name("yadhu"))

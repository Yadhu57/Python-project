class B:
    def __init__(self, name):
        print("parameterised constructor")
        self.na = name

    def __del__(self):
        print("Destructor")


ob = B('Arun')
del ob

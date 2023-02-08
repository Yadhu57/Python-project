# Eg1 passing mutable object

def change_string(str):
    str = str + " how are you"
    print("printing string inside the function:", str)


string1 = "Hi i am there"
change_string(string1)  # Function call
print("Printing outside the function:", string1)

print("__________________________________________________\n")
# Eg2 passing immutable object

def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("List inside function:", list1)


list1 = [10, 30, 40, 50]
change_list(list1)  # function call
print("List outside function:", list1)

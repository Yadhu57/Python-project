try:
    n = int(input("Enter first number:"))
    m = int(input("Enter second number:"))
    k = n/m
    print("Output is:", k)
# except ZeroDivisionError as er:    # er- just a variable name
#     print(er)
# except ValueError as j:
#     print(j)

# Exception class handles every errors
except Exception as er:
    print(er)

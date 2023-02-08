# 9.Define a function that accepts roll number and returns whether the student is present or absent.
def roll(a):
    if 1 <= a <= 20:
        print("Present")
    elif 21 <= a <= 40:
        print("Absent")
    else:
        print("Enter valid roll number")


a = int(input("Enter roll number"))
roll(a)

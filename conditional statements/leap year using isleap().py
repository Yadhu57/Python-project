import calendar
n = int(input("Enter the year"))
a = calendar.isleap(n)
if a:
    print(n, "is leap year")
else:
    print(n, "is not a leap year")


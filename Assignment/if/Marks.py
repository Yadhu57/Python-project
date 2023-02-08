physics = int(input("Enter your mark of physics"))
chemistry = int(input("Enter your mark of chemistry"))
biology = int(input("Enter your mark of biology"))
maths = int(input("Enter your mark of maths"))
computer = int(input("Enter your mark of computer"))
total = physics+chemistry+biology+maths+computer
percentage = total / 500 * 100
print("Total mark =", total)
if percentage < 40:
    print("Grade-F", "percentage-", percentage, "%")
elif 40 <= percentage < 60:
    print("Grade-E", "percentage-", percentage, "%")
elif 60 <= percentage < 70:
    print("Grade-D", "percentage-", percentage, "%")
elif 70 <= percentage < 80:
    print("Grade-C", "percentage-", percentage, "%")
elif 80 <= percentage < 90:
    print("Grade-B", "percentage-", percentage, "%")
elif percentage >= 90:
    print("Grade-A", "percentage-", percentage, "%")

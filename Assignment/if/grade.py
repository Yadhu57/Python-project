physics = int(input("Enter your mark of physics"))
chemistry = int(input("Enter your mark of chemistry"))
biology = int(input("Enter your mark of biology"))
maths = int(input("Enter your mark of maths"))
computer = int(input("Enter your mark of computer"))
a = (physics / 100) * 100
b = chemistry / 100 * 100
c = biology / 100 * 100
d = maths / 100 * 100
e = computer / 100 * 100

 #physics
if a < 40:
    print("Physics-", "F-", a, "%")
elif 40 <= a < 60:
    print("Physics-", "E-", a, "%")
elif 60 <= a < 70:
    print("Physics-", "D-", a, "%")
elif 70 <= a < 80:
    print("Physics-", "C-", a, "%")
elif 80 <= a < 90:
    print("Physics-", "B-", a, "%")
elif a >= 90:
    print("Physics-", "A-", a, "%")

 #chemistry

if b < 40:
    print("Chemistry-", "F-", b, "%")
elif 40 <= b < 60:
    print("Chemistry-", "E-", b, "%")
elif 60 <= b < 70:
    print("Chemistry-", "D-", b, "%")
elif 70 <= b < 80:
    print("Chemistry-", "C-", b, "%")
elif 80 <= b < 90:
    print("Chemistry-", "B-", b, "%")
elif b >= 90:
    print("Chemistry-", "A-", b, "%")

 # Biology

if c < 40:
    print("Chemistry-", "F-", c, "%")
elif 40 <= c < 60:
    print("Chemistry-", "E-", c, "%")
elif 60 <= c < 70:
    print("Chemistry-", "D-", c, "%")
elif 70 <= c < 80:
    print("Chemistry-", "C-", c, "%")
elif 80 <= c < 90:
    print("Chemistry-", "B-", c, "%")
elif c >= 90:
    print("Chemistry-", "A-", c, "%")

 #maths

if d < 40:
    print("Maths-", "F-", d, "%")
elif 40 <= d < 60:
    print("Maths-", "E-", d, "%")
elif 60 <= d < 70:
    print("Maths-", "D-", d, "%")
elif 70 <= d < 80:
    print("Maths-", "C-", d, "%")
elif 80 <= d < 90:
    print("Maths-", "B-", d, "%")
elif d >= 90:
    print("Maths-", "A-", d, "%")

 # Computer

if e < 40:
    print("Computer-", "F-", e, "%")
elif 40 <= e < 60:
    print("Computer-", "E-", e, "%")
elif 60 <= e < 70:
    print("Computer-", "D-", e, "%")
elif 70 <= e < 80:
    print("Computer-", "C-", e, "%")
elif 80 <= e < 90:
    print("Computer-", "B-", e, "%")
elif e >= 90:
    print("Computer-", "A-", e, "%")










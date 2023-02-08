# 4.Write a Python program to print a dictionary in table format.
dict1 = {1: ["Akhil", 21, 'Html'],
         2: ["Arun", 20, 'java'],
         3: ["Anoop", 21, 'python'],
         }
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))

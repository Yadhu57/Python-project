# 1.Remove empty strings from a list of strings
# Str1 = [“John”, “ ”,“Jack”,”Emma”,” ”,”Jins”,”Lina”]
# o/p: Str1 = [“John”,“Jack”,”Emma”,”Jins”,”Lina”]

str1 = ["John", "", "Jack", "Emma", "", "Jins", "Lina"]
i = 0
while i < len(str1):
    if len(str1[i]) == 0:
        str1.pop(i)
    i = i + 1
print(str1)

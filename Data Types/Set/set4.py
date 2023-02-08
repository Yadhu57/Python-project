# 3. Check if two sets have any elements in common,if yes,display the common elements.
a = {'p', 'y', 't', 'h', 'o', 'n'}
b = {'a', 'b', 'p', 'x', 'o', 'n', 'b', 't'}
if a & b:
    print("have common elements:", a & b)
else:
    print("No common elements")


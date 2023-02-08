import random
print(random.randint(1, 100))  # returns a random integer b/w the specified integers
print(random.randrange(1, 10))
print(dir(random))
n = [1, 2, 3, 4, 7, 9]
random.shuffle(n)
print(n)

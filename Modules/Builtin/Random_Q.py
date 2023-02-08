"""
write a program to generate a random color hex, a random alphabetical string,
random value between 2 integers, and random multiple of 7 b/w 0 to 70
hint: use random.randint()
"""
import random

rand = random.randint(0, 16777215)
hex_num = str(hex(rand))
hex_num = '#'+hex_num[2:]
print('random color hex', hex_num)


a = "STRING"
print(random.choice(a))

print("Random value b/w 2 integers:", random.randint(0, 10))

b = []
for i in range(0, 71):
    if i % 7 == 0:
        b.append(i)
print("Random multiple of 7:", random.choice(b))


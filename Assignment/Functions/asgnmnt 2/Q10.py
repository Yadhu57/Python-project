# 10.Define a function which counts vowels and consonant in a word
def fn(str1):
    str1 = str1.lower()
    c = 0
    v = 0
    for i in range(0, len(str1)):
        if str1[i] in ['a', 'e', 'i', 'o', 'u']:
            v = v + 1
        else:
            c = c + 1
    print('vowels:', v)
    print('consonants:', c)


str1 = input("Enter a word")
fn(str1)

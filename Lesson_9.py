list_1 = [15, 48, "hello", 6, 19, 'world']


def chet(s):
    summ = 0
    for j in str(s):
        summ += int(j)
    return summ


vowels = 0
consonants = 0

for i in list_1:
    if i == str(i):
        for j in i:
            if j in "aeiou":
                vowels += 1
            elif j in "bcdfghjklmnpqrstvwxyz":
                consonants += 1
        continue
    if i == int(i):
        if i % 2 == 0:
            a = list_1.index(i)
            list_1[a] = chet(i)
        else:
            a = list_1.index(i)
            list_1[a] = 1

print(list_1)
print(vowels, consonants)

import os

# 1
# with open('1.txt') as f:
#     file = f.readlines()
#     print(file)
# for i in file:
#     i = i.replace("_", " ")
#     b = i.split(" ")
# print(b)
# summ = 0
# for j in b:
#     if j.isdigit():
#         j = int(j)
#         summ += j
# print(summ)


# 2

# with open("2.txt") as f:
#     file = f.readlines()
#     print(file)
# number = []
# string = []
# for i in file:
#     i = i[:-1]
#     if i.isdigit():
#         i = int(i)
#         number.append(i)
#     elif i.isalpha():
#         i = str(i)
#         string.append(i)
# print(number)
# print(string)
# number.sort()
# string.sort()
# number.extend(string)
# print(number)

# 3
# file_name = input("name_file:")
# file = open(file_name, 'w')
# while True:
#     information = input("information:")
#     if information != " ":
#         file.write(information + "\n")
#     else:
#         break


# 4

# with open("4.txt") as f:
#     file = f.readlines()
#     print(file)
# print("Строк в файле:", len(file))
# st = 0
# for i in file:
#     st += 1
#     print(f"В строке {st} - {len(i)} символов.")

# 5

massiv = ["sdfsdf", "sdfdf", 345, 34, "hell", 7]
slova = []
cifri = []
massiv = [str(i) for i in massiv]
for i in massiv:
    if i.isalpha():
        slova.append(i)
    if i.isdigit():
        cifri.append(i)
slova.sort(key=len)
cifri.sort()
slova.extend(cifri)
f = open("DZ.txt", "w")
f.write(str(slova))
f.close()

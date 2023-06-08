# nec_znach = 1
# sume = 1
# while nec_znach < 30:
#     sume *= nec_znach
#     nec_znach += 2
# print(sume)


# nec_znach = 1
# sume = 1
# for i in range(1, 30, 2):
#     sume *= i
# print(sume)


# mass= []
# for i in range(0, 101, 5):
#     mass.append(i)
# print(mass)


# for i in range(2, 71, 2):
#     print(i)

# mass_1 = []
# n = int(input("Введите размер массива: "))
# for i in range(n):
#     ch = input("Введите значения массива: ")
#     mass_1.append(ch)
# new_mass = []
# for i in range(n):
#     if mass_1.count(mass_1[i]) >= 2:
#         new_mass.append(mass_1[i])
# print(new_mass)


# Программа проверяеет содержит ли введённое слово или набор символов строку проверки.

# num_1 = input("Введите слово или набор символов: ")
# num_2 = input("Введите строку проверки: ")
# count = 0
# for i in num_1:
#     if num_2 in num_1:
#         count += 1
# if count == len(num_1):
#     print("Проверка пройдена")
# else:
#     print("Проверка не пройдена")

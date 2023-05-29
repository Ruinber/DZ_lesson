# from random import*
#
# count = 0
# while count != 5:
#     comp_number = randint(1, 10)
#     comp_color = randint(1, 2)
#     number = int(input("Введите число от 1 доо 10: "))
#     color = int(input("Выберите цвет поля(1 - красное или 2 - черное): "))
#     if (number < 1 or number > 10) or (1 > color or color > 2):
#         print("Некорректный ввод")
#         break
#     elif number == comp_number and color == comp_color:
#         print("Вы выиграли")
#         break
#     else:
#          print("Вы проиграли. Верная комбинация:", comp_number, comp_color, "Попробуйте еще раз")
#     count += 1
#     if count == 5:
#         print("Это была последняя попытка. Повезёт в другой раз.")


num_1 = int(input())
num_2 = int(input())
if num_1 < 0 or num_2 < 0:
    while num_1 != 0 and num_2 != 0:
        if num_1 < num_2:
            print(num_1)
        else:
            print(num_2)
            num_2 += 1

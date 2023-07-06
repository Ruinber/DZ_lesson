import datetime
import math

# 1
# height = int(input("Укажите ваш рост: "))
# weight = int(input("Укажите ваш вес: "))
#
#
# def ves(mas, rost):
#     imt = mas / ((rost / 100) ** 2)
#     if imt <= 18.5:
#         return print("Недостаточная масса")
#     elif 18.5 <= imt <= 25:
#         return print("Масса в норме")
#     elif imt > 25:
#         return print("Избыточная масса")
#
#
# ves(weight, height)


# 2
# storon = int(input("Укажите количество сторон фигуры(3-10):"))
#
# def figure(st):
#     if st == 3:
#         return print("Ваша фигура это треугольник.")
#     elif st == 4:
#         return print("Ваша фигура это четырехугольник.")
#     elif st == 5:
#         return print("Ваша фигура это пятиугольник.")
#     elif st == 6:
#         return print("Ваша фигура это шестиугольник.")
#     elif st == 7:
#         return print("Ваша фигура это семиугольник.")
#     elif st == 8:
#         return print("Ваша фигура это восьмиугольник.")
#     elif st == 9:
#         return print("Ваша фигура это девятиугольник.")
#     elif st == 10:
#         return print("Ваша фигура это десятиугольник.")
#     else:
#         return print("Фигура вне диапазона.")
#
# figure(storon)

# 3
# year = int(input("Год:"))
# month = int(input("Месяц:"))
# day = int(input("День:"))
#
#
# def data(y, m, d):
#     now_date = datetime.date(y, m, d)
#     day_1 = datetime.timedelta(days=1)
#     new_data = now_date + day_1
#
#     return print(new_data)
#
#
# data(year, month, day)


# 4


# order_1 = 10.95
# other_orders = 2.95
#
# number_of_orders = int(input("Введите количество заказов:"))
#
# def order(kol_order):
#     if kol_order == 1:
#         return print("Стоимость покупки:", order_1)
#     elif kol_order >1:
#         return print("Стоимость покупки:", ('%.2f' % (order_1 +(other_orders*(number_of_orders-1)))))
#     else:
#         return print("Вы ничего не заказали")
#
# order(number_of_orders)


# 5

# numerator = int(input("Введите чиситель:"))
# denominator = int(input("Введите знаменатель:"))
#
# def fraction_reduction(numerator, denominator):
#     nod = math.gcd(numerator, denominator)
#     return print(int(numerator/nod), "/", int(denominator/nod))
#
# fraction_reduction(numerator, denominator)


# 6

spisok = []
lem = 1

for i in range(10):
    l = input(f'"Укажите 10 элементов списка №" {lem}:')
    spisok.append(l)
    lem +=1

def spisok_10(spisok):
    print(spisok.reverse())
    print(spisok[::-1])
    print(spisok[::])
    print(spisok[2:7])
    del spisok[5]
    print(spisok)

    for i in spisok:
        a = 0




    numbers = []
    letters = []
    for i in spisok:
        if i.isdigit():
            numbers.append(i)
        else:
            letters.append(i)
    numbers.extend()


spisok_10(spisok)


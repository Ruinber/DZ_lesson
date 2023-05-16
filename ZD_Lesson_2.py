#  Творческое задание
# Пользователь ввел свою дату рождения, но при вводе все цифры слились вместе.
# Выведите на экран корректную дату. (Гарантируется корректный ввод данных пользователем (Число из 8 цифр))

# date_birth = int(input())
# year = date_birth % 10000
# month = (date_birth // 10000) % 100
# day = date_birth // 1000000
# print(day, month, year, sep='.')

#Задача №1

# anna = 2
# pol = 5
# print("Яблок у Анны:", anna, "Яблок у Пола:", pol)


#Задача №2

# edge = int(input())
# volume = edge ** 3
# square_side_surface = 4 * edge ** 2
# print("Объем куба:", volume)
# print("Площадь боковой поверхности:", square_side_surface)


# Задача №3

height_tree = int(input("Высота дерева: "))
crawl_forward = int(input("Проползает за день: "))
crawl_back = int(input("Опускается за ночь: "))
days = (int(1 + (height_tree - crawl_back - 1) / (crawl_forward - crawl_back)))
print(days)









# task 1
# person = {"name": "pasha", "age": "45", "city": "Sochi"}
# print(person["age"])


# task 2
# car = {"BMV": [1, 2, 3], "Tesla": [4, 5, 6]}
# print(car["BMV"][0], car["BMV"][-1], car["Tesla"][0], car["Tesla"][-1])

# task 3
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# print(d1["b"] == d2["b"])


# task 4
# dictionary = {"a": 5, "b": 3, "c": 2}
# print(dictionary["a"] * dictionary["b"] * dictionary["c"])


# task 5
# list_1 = ["a", "b", "c", "d"]
# list_2 = [1, 2, 3, 3]
# dictionary = list(zip(list_1, list_2))
# print(dictionary)

# task 6
# stroka = "pythohist"
# dictionary = {i: stroka.count(i) for i in stroka}
# print(dictionary)


# task 7
# dictionary = {"apple": [5, 78], "lemon": [7, 45], "cabbage": [3, 35]}
# product_name = "0"
# count = 0
# while product_name != "n":
#     product_name = input("Выберите название продукта (apple, lemon, cabbage, n - end): ")
#     if product_name == "n":
#         break
#     number_of_products = int(input("Введите количество продуктов: "))
#     if product_name == "apple":
#         count += int(dictionary["apple"][-1]) * number_of_products
#         dictionary["apple"][-1] = (dictionary["apple"][-1] - number_of_products)
#     elif product_name == "lemon":
#         count += int(dictionary["lemon"][-1]) * number_of_products
#         dictionary["lemon"][-1] = (dictionary["lemon"][-1] - number_of_products)
#     elif product_name == "cabbage":
#         count += int(dictionary["cabbage"][-1]) * number_of_products
#         dictionary["cabbage"][-1] = (dictionary["cabbage"][-1] - number_of_products)
#     else:
#         print("Некорректный ввод")
#         continue
# print("Цена выбранных товаров", "-", count, "Осталось яблок:", "-", dictionary["apple"][-1], \
#       "Осталось лимонов:", "-", dictionary["lemon"][-1], "Осталось капусты:", "-", dictionary["cabbage"][-1])

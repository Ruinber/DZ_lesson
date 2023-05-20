from random import *

# Задание №9
# mister = input()
# if mister == "Mister":
#     print("Yes")
# else:
#     print("No")


# Задание №10
# armor_color = input("Enter armor color. Color options: red, yellow, black: ")
# if armor_color != "red" and armor_color != "yellow" and armor_color != "black":
#     print("Неверный цвет")
# shield_color = input("Enter shield color. Color options: red, yellow, black: ")
# if shield_color != "red" and shield_color != "yellow" and shield_color != "black":
#     print("Неверный цвет")
# if (armor_color == "yellow" or armor_color == "black") and shield_color == "black":
#     print(True)
# else:
#     print(False)


# Задание 1
# arbitrary_number = randint(1, 10)
# your_number = int(input("Enter a number from 1 to 10: "))
# if your_number <= 0 and your_number >= 11:
#     print("Invalid input")
# if arbitrary_number == your_number:
#     print("You won")
# else:
#     print("You lost")


# Задание 2
# day_your_birthday = int(input("Day your birthday: "))
# month_of_your_birth = int(input("Month of your birth: "))
# if 1 <= day_your_birthday <= 31 and 3 <= month_of_your_birth <= 4:
#     print("your zodiac sign is Aries")
# elif 1 <= day_your_birthday <= 31 and 4 <= month_of_your_birth <= 5:
#     print("your zodiac sign is Taurus")
# elif 1 <= day_your_birthday <= 31 and 5 <= month_of_your_birth <= 6:
#     print("your zodiac sign is Gemini")
# elif 1 <= day_your_birthday <= 31 and 6 <= month_of_your_birth <= 7:
#     print("your zodiac sign is Cancer")
# elif 1 <= day_your_birthday <= 31 and 7 <= month_of_your_birth <= 8:
#     print("your zodiac sign is Leo")
# elif 1 <= day_your_birthday <= 31 and 8 <= month_of_your_birth <= 9:
#     print("your zodiac sign is Virgo")
# elif 1 <= day_your_birthday <= 31 and 9 <= month_of_your_birth <= 10:
#     print("your zodiac sign is Libra")
# elif 1 <= day_your_birthday <= 31 and 10 <= month_of_your_birth <= 11:
#     print("your zodiac sign is Scorpio")
# elif 1 <= day_your_birthday <= 31 and 11 <= month_of_your_birth <= 12:
#     print("your zodiac sign is Sagittarius")
# elif 1 <= day_your_birthday <= 31 and (month_of_your_birth == 12 or month_of_your_birth == 1):
#     print("your zodiac sign is Capricorn")
# elif 1 <= day_your_birthday <= 31 and 1 <= month_of_your_birth <= 2:
#     print("your zodiac sign is Aquarius")
# elif 1 <= day_your_birthday <= 31 and 2 <= month_of_your_birth <= 3:
#     print("your zodiac sign is Pisces")
# else:
#     print("invalid input")


# Задача 3
# Введите время (час и минуту) и узнайте чей сейчас час.
hour = int(input("Enter a number from 0 to 24: "))
minute = int(input("Enter a number from 0 to 59: "))
if (hour == 23 and 0 <= minute < 60) or ((hour == 0 or hour == 24) and 0 <= minute < 60):
    print("Hour of the Rat")
elif 1 <= hour <= 2 and 0 <= minute < 60:
    print("Hour of the Ox")
elif 3 <= hour <= 4 and 0 <= minute < 60:
    print("Hour of the Tiger")
elif 5 <= hour <= 6 and 0 <= minute < 60:
    print("Hour of the Rabbit")
elif 7 <= hour <= 8 and 0 <= minute < 60:
    print("Hour of the Dragon")
elif 9 <= hour <= 10 and 0 <= minute < 60:
    print("Hour of the Snake")
elif 11 <= hour <= 12 and 0 <= minute < 60:
    print("Hour of the Horse")
elif 13 <= hour <= 14 and 0 <= minute < 60:
    print("Hour of the Sheep")
elif 15 <= hour <= 16 and 0 <= minute < 60:
    print("Hour of the Monkey")
elif 17 <= hour <= 18 and 0 <= minute < 60:
    print("Hour of the Rooster")
elif 19 <= hour <= 20 and 0 <= minute < 60:
    print("Hour of the Dog")
elif 21 <= hour <= 22 and 0 <= minute < 60:
    print("Hour of the Pig")
else:
    print("invalid input")

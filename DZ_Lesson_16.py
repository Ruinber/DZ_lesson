
while True:
    try:
        num_1 = input("Число 1:")
        num_2 = input("Число 2:")
        if num_1.isdigit() and num_1.isdigit():
            dell = int(num_1)/int(num_2)
            print(dell)
            break
        elif num_2 == 0:
            continue
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Введите цифры")



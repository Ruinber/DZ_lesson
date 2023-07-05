# tuple_1 = ("sdfsdf", "sdfsdf", "sdfdsf")
# list_1 = ["sdf", 3, 4, 45, "sdfs"]
# number_1 = 242336545
str_1 = "good weat"


def dlin_slov(a):
    count = 0
    if (isinstance(a, tuple)):
        for i in a:
            count += len(i)
        return print("Длинна всех слов:",count)
    letters = 0
    numbers = 0
    if (isinstance(a, list)):
        for j in a:
            if (isinstance(j, int)):
                numbers += 1
            elif (isinstance(j, str)):
                letters += len(j)
        return print(f" чисел - {numbers}, букв - {letters}")
    if (isinstance(a, int)):
        for k in range(0, len(str(a)) + 1, 2):
            count += 1
        return print("Количество нечетных цифр:", count)
    if (isinstance(a, str)):
        for char in a:
            count += 1
        return print("Количество букв:", count)


dlin_slov(str_1)

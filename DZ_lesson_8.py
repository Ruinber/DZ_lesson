def sign_plus(n1, n2):
    return n1 + n2
def sign_minus(n1, n2):
    return n1 - n2
def sign_multiply(n1, n2):
    return n1 * n2
def sign_divide(n1, n2):
    return n1 / n2





num2 = ''

while num2 != 0:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    sign = input("Ведите знак операции: ")
    if sign == "+":
        print(sign_plus(num1, num2))
        continue
    elif sign == "-":
        print(sign_minus(num1, num2))
        continue
    elif sign == "*":
        print(sign_multiply(num1, num2))
        continue
    elif sign == "/":
        if num2 != 0:
            print(sign_divide(num1, num2))
        else:
            break











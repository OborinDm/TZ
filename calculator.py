
while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        digit = input("Введите значение (+-*/): ")
        if digit == "+":
            print(a + b)
        elif digit == "-":
            print(a - b)
        elif digit == "*":
            print(a * b)
        elif digit == "/":
            print(a / b)
        else:
            print("Не определено")
    except ValueError:
        print("Ошибка!")
    except ZeroDivisionError:
        print("Ошибка!")



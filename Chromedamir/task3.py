try:
    # Ввод сторон
    a = float(input("a: "))
    b = float(input("b: "))
    
    # Проверка и вычисление
    if a > 0 and b > 0:
        S = a * b
        P = 2 * (a + b)
        print(f"S = {S}")
        print(f"P = {P}")
    else:
        print("Ошибка: Стороны должны быть положительными.")
except ValueError:
    print("Ошибка: Введите число.")
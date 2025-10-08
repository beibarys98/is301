# Даны целые положительные числа A и B (A > B)
A = int(input("Введите длину отрезка A: "))
B = int(input("Введите длину отрезка B: "))

# Длина незанятой части отрезка A
unoccupied_length = A % B

print("Длина незанятой части отрезка A:", unoccupied_length)
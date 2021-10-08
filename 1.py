try:
    n = int(input('Введите количество элементов в массиве: '))
    B = [0] * n
    for i in range(n):
        B[i] = int(input('Введите значения элементов: '))
    delta = int(input('Введите значение дельта: '))
    result = B.count(min(B) + delta)
    print(f'{result} элемент(ов) соответсвует условию')
except ValueError:
    print('Это не число. Введите число.')
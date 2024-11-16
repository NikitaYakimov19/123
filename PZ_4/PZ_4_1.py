"""Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
целые степени числа A от 1 до N."""
try:
    A = int(input("Введите вещественное число A: "))
    # Запрашиваем у пользователя значение N (целое число > 0)
    N = int(input("Введите целое число N (>0): "))
    if N <= 0:
        raise ValueError("Параметр N должен быть больше 0.")
    # Цикл от 1 до N включительно
    for i in range(1, N + 1):
        # Вычисляем A в степени i
        stepen = A ** i
        # Выводим результат в формате "A ^ i = power"
        print(A, "^", i, " = ", stepen)
except ValueError as e:
    # Обрабатываем ошибки преобразования ввода
    print("Ошибка.", e)

'''Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
Проверить истинность высказывания: «Треугольник со сторонами a, b, c является
прямоугольным».'''
try:
    # Запрашиваем ввод значений для сторон треугольника
    a = int(input("Введите a = "))  # Сторона a
    b = int(input("Введите b = "))  # Сторона b
    c = int(input("Введите c = "))  # Сторона c

    # Проверяем, является ли треугольник прямоугольным по теореме Пифагора
    if a ** 2 == b ** 2 + c ** 2:
        print("Треугольник прямоугольный")
    elif b ** 2 == a ** 2 + c ** 2:
        print("Треугольник прямоугольный")
    elif c ** 2 == a ** 2 + b ** 2:
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не является прямоугольным")

except ValueError:
    # Обрабатываем случай, если введены некорректные значения
    print("Ошибка: Пожалуйста, введите целые числа для сторон треугольника.")
except Exception as e:
    # Обрабатываем любые другие исключения
    print(f"Произошла ошибка: {e}")

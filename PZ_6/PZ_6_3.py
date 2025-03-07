"""Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1)."""

a = input("Введите список чисел, разделенных запятыми: ")
# Проверка на наличие запятых
if ',' not in a:
    print("Ошибка: Введите числа, разделенные запятыми.")
else:
    a = a.split(',')
    a = [int(num.strip()) for num in a]  # Преобразуем каждое число в целое
    print("Вы ввели этот список: ", a)

    if len(a) > 0:  # Проверяем, что список не пустой
        # Сохраняем последний элемент
        last_element = a[-1]
        # Индекс для сдвига элементов
        i = len(a) - 1

        # Сдвигаем все элементы вправо на одну позицию
        while i > 0:
            a[i] = a[i - 1]
            i -= 1

        # Устанавливаем последний элемент на первое место
        a[0] = last_element

    print("Вот такой список получился после сдвига вправо ", a)

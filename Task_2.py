n = 1 + int(input('Введите число раз, когда мужчина передумал идти в выбранную им сторону (дом или работа): '))


def f():
    distance_travelled = 0
    spacing_between = 0
    for i in range(1, n + 1):
        distance_travelled += 1000 / i
        spacing_between += (1000 / i) * ((-1) ** (i + 1))
    print('Мужчина прошёл ', int(round(distance_travelled, 0)), 'м.')
    print('Расстояние между ним и домом составляет ', int(round(spacing_between, 0)), 'м.')


f()

input()

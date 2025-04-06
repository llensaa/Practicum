x_first = float(input('Координаты по Х первой окружности: '))
y_first = float(input('Координаты по Y первой окружности: '))
r_first = float(input('R первой окружности: '))
x_second = float(input('Координаты по Х второй окружности: '))
y_second = float(input('Координаты по Y второй окружности: '))
r_second = float(input('R второй окружности: '))

distance = ((x_second - x_first) ** 2 + (y_second - y_first) ** 2) ** 0.5
if distance > r_first + r_second:
    print('Окружности лежат одна вне другой, не касаясь')
elif distance < abs(r_first - r_second):
    print('Одна окружность лежит внутри другой, не касаясь')
elif distance == r_first + r_second:
    print('Окружности имеют внешнее касание')
elif distance == abs(r_first - r_second):
    print('Окружности имеют внутреннее касание')
else:
    print('Окружности пересекаются')
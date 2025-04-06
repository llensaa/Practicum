x1_l, y1_u = map(int, input().split())
x1_r, y1_d = map(int, input().split())
x2_l, y2_u = map(int, input().split())
x2_r, y2_d = map(int, input().split())
if x1_r < x2_l or x2_r < x1_l or y2_u < y1_d or y1_u < y2_d:
    print('Прямоугольники лежат вне друг-друга, не касаясь')
elif (x1_r == x2_l or x1_l == x2_r) and (y1_d < y2_u and y1_u > y2_d):
    print('Прямоугольники имеют касание')
elif (y1_u == y2_d or y1_d == y2_u) and (x1_l < x2_r and x1_r > x2_l):
    print("Прямоугольники имеют касание")
elif (x1_l > x2_l and x1_r < x2_r and y1_d > y2_d and y1_u < y2_u):
    print("Первый прямоугольник полностью внутри второго, не касаясь")
elif (x2_l > x1_l and x2_r < x1_r and y2_d > y1_d and y2_u < y1_u):
    print("Второй прямоугольник полностью внутри первого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")
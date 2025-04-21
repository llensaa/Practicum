import math

square = list(map(int, input().split("x")))
a = square[0]
b = square[1]

arena_diameter = 2 * 6.5
diagonal = math.sqrt(a ** 2 + b ** 2)
if diagonal <= arena_diameter:
    print("да")
else:
    print("нет")
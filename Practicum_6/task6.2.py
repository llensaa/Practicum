square = list(map(int, input().split("x")))
A = square[0]
B = square[1]

volume = list(map(int, input().split("x")))
C = volume[0]
D = volume[1]
E = volume[2]

hole = A * B
brick_1 = C * E
brick_2 = E * D
brick_3 = C * D

if brick_1 < hole or brick_2 < hole or brick_3 < hole:
    print("да")
else:
    print("нет")
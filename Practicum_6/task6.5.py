turn = input().split("-")
forward = turn[0]
side = turn[1]

literal_f = forward[0]
number_f = int(forward[1])
literal_s = side[0]
number_s = int(side[1])

if abs(ord(literal_s) - ord(literal_f)) == 1:
    if abs(number_s - number_f) == 2:
        print("верно")
    else:
        print("ошибка")
elif abs(ord(literal_s) - ord(literal_f)) == 2:
    if abs(number_s - number_f) == 1:
        print("верно")
    else:
        print("ошибка")
else:
    print("ошибка")
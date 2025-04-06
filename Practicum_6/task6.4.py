chess_square = input()
literal = chess_square[0]
number = int(chess_square[1])

even = ["b", "d", "f", "h"]
uneven = ["a", "c", "e", "g"]

if literal in even:
    if number % 2 != 0:
        print("белый")
    else:
        print("черный")
if literal in uneven:
    if number % 2 != 0:
        print("черный")
    else:
        print("белый")
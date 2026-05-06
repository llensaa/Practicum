import random


class NavalBattle:
    playing_field = None
    shots = None

    def __init__(self, symbol):
        self.symbol = symbol
        if NavalBattle.shots is None:
            NavalBattle.shots = [['~'] * 10 for _ in range(10)]

    @staticmethod
    def show():
        if NavalBattle.shots is None:
            print("игровое поле не заполнено")
            return

        for row in NavalBattle.shots:
            print(' '.join(row))
        print()

    def shot(self, x, y):
        if NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return

        x -= 1
        y -= 1

        if NavalBattle.shots[x][y] != '~':
            print("ошибка")
            return

        if NavalBattle.playing_field[x][y] == 1:
            NavalBattle.shots[x][y] = self.symbol
            print("попал")
        else:
            NavalBattle.shots[x][y] = 'o'
            print("мимо")

    @staticmethod
    def new_game():
        field = [[0]*10 for _ in range(10)]

        def can_place(x, y):
            for i in range(max(0, x-1), min(10, x+2)):
                for j in range(max(0, y-1), min(10, y+2)):
                    if field[i][j] == 1:
                        return False
            return True

        def place_ship(size):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.choice([(1, 0), (0, 1)])

                coords = []
                for k in range(size):
                    nx = x + direction[0]*k
                    ny = y + direction[1]*k

                    if not (0 <= nx < 10 and 0 <= ny < 10):
                        break
                    if not can_place(nx, ny):
                        break

                    coords.append((nx, ny))

                if len(coords) == size:
                    for nx, ny in coords:
                        field[nx][ny] = 1
                    break

        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for s in ships:
            place_ship(s)

        NavalBattle.playing_field = field
        NavalBattle.shots = [['~'] * 10 for _ in range(10)]
class NavalBattle:
    playing_field = [[0]*10 for _ in range(10)]
    shots = [['~']*10 for _ in range(10)]

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        for row in NavalBattle.shots:
            print(' '.join(row))
        print()

    def shot(self, x, y):
        x -= 1
        y -= 1

        if NavalBattle.playing_field[x][y] == 1:
            NavalBattle.shots[x][y] = self.symbol
            print("попал")
        else:
            NavalBattle.shots[x][y] = 'o'
            print("мимо")
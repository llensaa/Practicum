data = list(map(int, input().split()))
X = data[0]
Y = data[1]
N = data[2]
revenue = N * ((X * 100) + Y)
rub = revenue // 100
kop = revenue % 100
print(f'{rub} руб. {kop} коп.')
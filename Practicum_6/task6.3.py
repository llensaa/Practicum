n, m = map(int, input().split("x"))
k = int(input())
COUNT = 0

if k < m * n:
    for line in range(1, n):
        if (line * m) >= k and ((n - line) * m) >= (n * m - k):
            COUNT += 1
    for col in range(1, m):
        if (col * n) >= k and ((m - col) * n) >= (n * m - k):
            COUNT += 1
else:
    print(f'Некорректный ввод')

if COUNT > 0:
    print(f'Успешно')
else:
    print(f'Неосуществимо')
num = int(input())
n = abs(num)
div = set()

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        div.add(i)
        div.add(n // i)

print(*div)
num = int(input())
counter = 0
for i in range(1, num):
    for j in range(1, i):
        if j**2 + i**2 == num:
            counter += 1
        elif i == j:
            counter -= 1
print(counter)
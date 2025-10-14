counter = 0
while True:
    n = int(input())
    if n % 4 == 0 and n != 0:
        counter += 1
    if n == 0:
        break
print(counter)
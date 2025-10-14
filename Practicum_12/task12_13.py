tickets = []
i = 1

while True:
    t = input()
    tickets.append(t)
    if len(t) % 2 == 0:
        mid = len(t)//2
        sum1 = sum(int(j) for j in t[:mid])
        sum2 = sum(int(j) for j in t[mid:])
        if sum1 == sum2:
            print(i)
            break
    i += 1

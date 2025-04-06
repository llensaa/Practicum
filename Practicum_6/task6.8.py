a = [str(i) for i in range(0, 201)]
b = list()
for i in a:
    x = [int(j) for j in i]
    for k in x:
        b.append(k)

print(b[int(input()) - 1])
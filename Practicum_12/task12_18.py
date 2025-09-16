s = input()
n = int(input())

words = s.split()
line = []
length = 0

for w in words:
    if length + len(line) + len(w) <= n:
        line.append(w)
        length += len(w)
    else:
        spaces = n - length
        if len(line) == 1:
            print(line[0] + ' ' * spaces)
        else:
            base, extra = divmod(spaces, len(line) - 1)
            for i in range(len(line) - 1):
                print(line[i], end=' ' * (base + (1 if i < extra else 0)))
            print(line[-1])
        line = [w]
        length = len(w)

    print(" ".join(line) + ' ' * (n - length - (len(line)-1)))
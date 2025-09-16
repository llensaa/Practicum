s = input()
words = s.split()

counts = {}
for i in words:
    if i not in counts:
        counts[i] = 0
    counts[i] += 1

for i in counts:
    if counts[i] > 1:
        print(i)

s = input()
words = s.split()

winner = ""
for i in range(len(words) - 1):
    if words[i][-1] != words[i + 1][0].lower():
        if i % 2 == 0:
            winner = "Петя"
        else:
            winner = "Вася"
        break
else:
    if (len(words) - 1) % 2 == 0:
        winner = "Петя"
    else:
        winner = "Вася"

print(winner)
K = int(input())
N = 0
M = 0
for i in range(K // 5):
    if (K - (i * 5)) % 7 == 0:
        N = "да"
        break
for j in range(K // 7):
    if (K - (j * 7)) % 5 == 0:
        M = "да"
        break
if M == "да" or N == "да":
    print("да")
else:
    print("нет")
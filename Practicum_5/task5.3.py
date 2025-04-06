number = input()
num = [i for i in number]
count = 0
for j in range(len(number) // 2):
    if num[j] == num[-j-1]:
        count += 1
if count == len(number) // 2:
    print("настоящее")
else:
    print("кривое")
num = int(input())
group = 1
while True:
    group += 1
    num_1 = num % group
    if num_1 == 0:
        break
print(group)
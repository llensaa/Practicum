numbers = list(map(int, input().split()))
num = []
for i in range(1, 9):
    num.append(numbers[i - 1] + numbers[i + 1])
print(num)
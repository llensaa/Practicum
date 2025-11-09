numbers = list(input().split())
index = numbers.index('3')
num = numbers.pop(index)
print(*numbers)
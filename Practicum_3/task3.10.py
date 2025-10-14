num = list(map(int, input().split()))
print(int((num[0] % num[1] == 0) + (num[1] % num[0] == 0)))
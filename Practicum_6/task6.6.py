import math

data = list(map(int, input().split()))
N = data[0]
K = data[1]
M = data[2]

minutes = (math.ceil((N * 2) / K)) * M
print(minutes)
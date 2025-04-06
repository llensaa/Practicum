heights = list(map(int, input().split()))
N = heights[0]
K = heights[1]
M = heights[2]
if N >= K and N >= M:
    if K >= M:
        print(N, K, M)
    else:
        print(N, M, K)
elif K >= N and K >= M:
    if N >= M:
        print(K, N, M)
    else:
        print(K, M, N)
else:
    if K >= N:
        print(M, K, N)
    else:
        print(M, N, K)
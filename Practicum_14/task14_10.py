lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start, end = map(int, input().split())
start_idx = start - 1
end_idx = end - 1

for i in range(end_idx + 1, start_idx - 1, -1):
    element = lst1.pop(i)
    lst2.append(element)

print(*lst1)
print(*lst2)
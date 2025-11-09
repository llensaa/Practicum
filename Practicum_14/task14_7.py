numbers = list(map(int, input().split()))
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'Четные - {sum(even)}, нечетные - {sum(odd)}')
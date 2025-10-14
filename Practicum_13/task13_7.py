def multiple(A, B, N):
    c = min(A, B)
    mult = set()
    for i in range(1, int(c ** 0.5) + 1):
        if A % i == 0 and B % i ==0:
            if i <= N:
                mult.add(i)
            if c // i <= N:
                mult.add(c // i)
    return mult

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
N = int(input('Введите число N: '))
print(multiple(A, B, N))
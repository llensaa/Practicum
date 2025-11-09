def p(x) -> bool:
    if x == 1:
        return False
    for k in range(2, int(x ** 0.5) + 1):
        if x % k == 0:
            return False
    return True

N = int(input('Введите N: '))
num_list = [i for i in range(1, N + 1) if p(i)]
print(num_list)
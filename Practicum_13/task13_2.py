def fibonacci(n) -> None:
    list = [1, 1]
    for i in range(n - 2):
        list.append(list[-1] + list[-2])
    print(list)

n = int(input('Введите N: '))
fibonacci(n)
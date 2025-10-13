def numbers(A, B):
    set_num = {1,3,4,8,9}
    list_num = []
    for i in range(min(A, B), max(A, B) + 1):
        numbers = {int(j) for j in str(i)}
        if numbers.issubset(set_num):
            list_num.append(i)
    print(list_num)

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
numbers(A, B)
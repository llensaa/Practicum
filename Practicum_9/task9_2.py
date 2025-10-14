num = int(input())
x = num
while x > 2:
    x = num ** 0.5
    print(f'{x:5.3f}')
    num = x
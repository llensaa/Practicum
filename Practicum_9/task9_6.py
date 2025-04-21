for i in range(10,100):
    if i ** 2 % 100 == i:
        break
print(f'{i:>3}\n*{i}\n___\n{i**2}')
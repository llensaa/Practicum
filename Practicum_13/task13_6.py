def message(str):
    if len(str) > 160:
        str = str[:160]
    return str

str = input('Введите сообщение: ')
print(message(str))
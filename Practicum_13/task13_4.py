def make_payment(P) -> None:
    if 20 <= P <= 1000:
        print('Успех')
    else: 
        print('Повторить попытку')

P = int(input('Введите сумму платежа: '))
make_payment(P)
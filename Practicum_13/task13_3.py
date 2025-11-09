def sales(price, card, day) -> float:
    sale = 0
    if 5000 <= price < 15000:
        sale += 3
    elif 15000 <= price < 20000:
        sale += 5
    elif 20000 <= price < 30000:
        sale += 7
    elif price >= 30000:
        sale += 10
    if card.lower() == 'да':
        sale += 5
    elif day.lower() == 'да':
        sale += 3
    if sale > 15:
        sale = 15
    end_price = round(price - (price * (sale / 100)), 2)

    return end_price

price = int(input('Введите цену товара: '))
card = input('Являетесь ли вы обладателем ' \
                'дисконтной карты? (да/нет)? ')
day = input('Сегодня празничный день?(да/нет)? ')
print(sales(price, card, day))
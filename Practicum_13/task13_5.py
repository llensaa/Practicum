def card(price) -> int:
    match price:
        case 5 | 10:
            price = price
        case 25:
            price += 3
        case 50:
            price += 8
        case 100:
            price += 20
    return price

price = int(input('Введите стоимость карты: '))
card(price)
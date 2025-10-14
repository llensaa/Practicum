money = int(input())
if money >= 17 * 29:
    g = money // (29 * 17)
    s = (money % (29 * 17) // 29)
    k = (money % (29 * 17) % 29) - s
    if s != 0:
        if k != 0:
            print(f"{g} галлеонов, {s} сиклей, {k} кнатов")
        else:
            print(f"{g} галлеонов, {k} кнатов")
    else:
        if k != 0:
            print(f"{g} галлеонов, {k} кнатов")
        else:
            print(f"{g} галлеонов")
elif money >= 29 and money < 17 * 29:
    s = money // 29
    k = (money % 29) - s
    if k != 0:
        print(f"{s} сиклей, {k} кнатов")
    else:
        print(f"{s} сиклей")
else: 
    k = money
    if k!= 0:
        print(f"{k} кнатов")
    else:
        print("Денег нет((((")
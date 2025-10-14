import re

def letters(str): 
    text = re.sub(r'[^А-Яа-я]', '', str.lower())
    counter_vow = 0
    counter_con = 0
    vowels = ['а', 'е','и', 'о','я',
                'ы','э', 'у','ё', 'ю']
    for i in text:
        if i in vowels:
            counter_vow += 1
        else:
            counter_con +=1
    print(f'Гласные: {counter_vow}, согласные: {counter_con}')

str = input('Введите предложение: ')
letters(str)
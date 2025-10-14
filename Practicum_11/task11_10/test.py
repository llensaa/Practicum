import datetime as dt


with open('Practicum/Practicum_11/task11_10/input.txt', 'r', encoding='utf-8') as file:
    lines_list = [line.strip() for line in file if line.strip()]

if len(lines_list) < 2:
    raise ValueError('Файл содержит слишком мало данных')

current_year = f'.{dt.datetime.today().year}'
current_date = dt.datetime.strptime(
    lines_list[0] + current_year,
    '%d.%m.%Y'
).date()

with open('Practicum/Practicum_11/task11_10/output.txt', 'w', encoding='utf-8') as output_file:
    for i in lines_list[2:]:
        parts = i.split()
        if len(parts) < 2:
            continue
        box_num, date_str = parts
        date = dt.datetime.strptime(date_str + current_year, '%d.%m.%Y').date()
        time_difference = current_date - date
        if time_difference > dt.timedelta(days=3):
            output_file.write(f'{box_num}\n')
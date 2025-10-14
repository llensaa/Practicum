with open('Practicum/Practicum_11/task11_7/input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    lines = info.split('\n')
    filtered_lines = [i for i in lines if int(i) != 100]
with open('Practicum/Practicum_11/task11_7/input.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(filtered_lines))
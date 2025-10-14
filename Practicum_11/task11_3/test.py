with open('Practicum/Practicum_11/task11_3/input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    lines = info.split('\n')
    filtered_lines = [i[0] for i in lines]
with open('Practicum/Practicum_11/task11_3/output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(''.join(filtered_lines))
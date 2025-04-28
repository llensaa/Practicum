with open('Practicum/Practicum_11/task11_2/input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    lines = info.split('\n')
    filtered_lines = [i for i in lines if i and i[0] == 'a' or i and i[0] == 'A']
with open('Practicum/Practicum_11/task11_2/output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(filtered_lines))
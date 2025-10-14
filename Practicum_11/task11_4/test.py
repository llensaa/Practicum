with open('Practicum/Practicum_11/task11_4/input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    lines = info.split('\n')
    filtered_lines = [i for i in lines if len(i) > 20]
with open('Practicum/Practicum_11/task11_4/output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(filtered_lines))
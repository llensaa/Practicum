with open('Practicum/Practicum_11/task11_1/input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    content = info.upper()
with open('Practicum/Practicum_11/task11_1/output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(content)
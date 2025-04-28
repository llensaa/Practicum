with open('Practicum/Practicum_11/task11_5/input.txt', 'r', encoding='utf-8') as file:
    line_list = []
    with open('Practicum/Practicum_11/task11_5/output.txt', 'w', encoding='utf-8') as output_file:
        try:
            for line in file:
                line_list.append(line)
            if (len(line_list) - 1) == int(line_list[0]):
                output_file.write('YES')
            else:
                output_file.write('NO')
        except ValueError:
            output_file.write('ERROR')
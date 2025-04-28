with open('Practicum/Practicum_11/task11_5/input.txt', 'r', encoding='utf-8') as file:
    num_list = []
    with open('Practicum/Practicum_11/task11_5/output.txt', 'w', encoding='utf-8') as output_file:
        try:
            for line in file:
                num = float(line)
                num_list.append(num)
            output_file.write(str(num_list[0] / num_list[1] + num_list[2]))
        except ZeroDivisionError:
            output_file.write('division by 0')
        except ValueError:
            output_file.write('data error')
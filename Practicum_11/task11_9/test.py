import os

base_dir = 'Practicum/Practicum_11/task11_9'
target_dir = os.path.join(base_dir, 'simple')

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

input_path = os.path.join(base_dir, 'input.txt')
with open(input_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

output_path = os.path.join(target_dir, 'output.txt')
with open(output_path, 'w', encoding='utf-8') as o:
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            o.write(line)
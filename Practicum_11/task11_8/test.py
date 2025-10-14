with open('Practicum/Practicum_11/task11_8/input.txt', 'r', encoding='utf-8') as file:
    steps_list = [int(line.strip()) for line in file]

months = [
    (steps_list[:31], 31),
    (steps_list[31:59], 28),
    (steps_list[59:90], 31),
    (steps_list[90:120], 30),
    (steps_list[120:151], 31),
    (steps_list[151:181], 30),
    (steps_list[181:212], 31),
    (steps_list[212:243], 31),
    (steps_list[243:273], 30),
    (steps_list[273:304], 31),
    (steps_list[304:334], 30),
    (steps_list[334:365], 31)
]

with open('Practicum/Practicum_11/task11_8/output.txt', 'w', encoding='utf-8') as output_file:
    for days, divisor in months:
        avg = sum(days) / divisor
        output_file.write(f"{avg:.2f}\n")
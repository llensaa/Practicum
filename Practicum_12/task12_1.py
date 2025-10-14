text = input("Введите текст: ")

max_count = 0
current_count = 0

for i in text:
    if i.isspace():
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)
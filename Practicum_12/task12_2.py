text = input()

if not text:
    print("Максимальное количество последовательных одинаковых символов: 0")
else:
    max_count = 1
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1

    print("Максимальное количество последовательных одинаковых символов:", max_count)

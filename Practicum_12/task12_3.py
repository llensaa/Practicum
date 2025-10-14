text = input("Введите текст: ")

letters = set()

for char in text:
    if char.isalpha():
        letters.add(char.lower())

print("Количество различных букв:", len(letters))

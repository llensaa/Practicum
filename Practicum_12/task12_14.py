hint = input()
word = input()

print("\n" * 25)
hidden_word = ["*"] * len(word)
attempts = 10

print(hint)
while attempts > 0:
    print("".join(hidden_word))
    answer = input("Буква или слово (0 - буква, 1 - слово)? ")
    if answer == "0":
        letter = input()
        for i, c in enumerate(word):
            if c == letter:
                hidden_word[i] = c
        if "".join(hidden_word) == word:
            print("Победа!")
            break
    else:
        guess = input()
        if guess == word:
            print("Победа!")
            break
        else:
            print("Проигрыш!")
            break
    attempts -= 1
else:
    print("Проигрыш!")

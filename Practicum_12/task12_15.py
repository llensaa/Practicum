number = input()
print("\n" * 25)

attempts = 10
while attempts > 0:
    guess = input()
    bulls = sum(i == j for i, j in zip(number, guess))
    cows = sum(min(number.count(k), guess.count(k)) for k in set(guess)) - bulls
    print(f"Быков: {bulls} Коров: {cows}")
    if bulls == len(number):
        print("Победа!")
        break
    attempts -= 1
else:
    print("Проигрыш!")

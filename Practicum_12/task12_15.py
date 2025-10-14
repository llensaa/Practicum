secret = input()
print("\n" * 25)

attempts = 10
while attempts > 0:
    guess = input()
    bulls = sum(a == b for a, b in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    print(f"Быков: {bulls} Коров: {cows}")
    if bulls == len(secret):
        print("Победа!")
        break
    attempts -= 1
else:
    print("Проигрыш!")

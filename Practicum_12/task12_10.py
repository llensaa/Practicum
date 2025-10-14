s = input()
words = s.split()
first_word = words[0]

for i in words:
    if i != first_word and len(i) == len(set(i)):
        print(i)
import re

sentence = input()
words = re.findall(r'[A-Za-zА-Яа-я]+', sentence)
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)
import re

def clean_word(word):
    return re.sub(r'[^\w]', '', word.lower())

text_lines = []
while True:
    line = input().strip()
    if line == "":
        break
    text_lines.append(line)

full_text = " ".join(text_lines)

words = full_text.split()
cleaned_words = [clean_word(word) for word in words if word]

word_count = {}
for word in cleaned_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_freq = list(word_count.items())

sorted_words = sorted(word_freq, key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(word)
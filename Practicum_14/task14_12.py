def count_holes_letters(word) → int:
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    count = 0
    for i in word:
        if i in holes_letters:
            count += 1
    return count

text = input().strip()
words = text.split()
total_holes = 0
total_no_holes = 0
holes_words = []

for word in words:
    holes_in_word = count_holes_letters(word)
    total_holes += holes_in_word
    total_no_holes += len(word) - holes_in_word
        
    if holes_in_word >= 2:
        holes_words.append(word)
    
print(total_holes, total_no_holes)
print(holes_words)

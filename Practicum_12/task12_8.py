s = input()
words = s.split()
words.sort(key=len)
print(" ".join(words))
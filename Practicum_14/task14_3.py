import re

sentence = input()
words = re.findall(r'[\w]+', sentence)
print(*words)
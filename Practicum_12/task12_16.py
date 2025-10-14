from re import *

s = input()

while list(finditer(r'\(\)', s)):
    s = sub(r'\(\)', '', s)

if '(' in s or ')' in s:
    print("Неправильно")
else:
    print("Правильно")

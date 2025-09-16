'''
text = input()

letters = set()

for char in text:
    if char.isalpha():
        letters.add(char.lower())

print("Количество различных букв:", len(letters))
'''

from re import *

s = input()
reg_ex = r'[А-Яа-яA-Za-z]'

letters = set()
for r_item in finditer(reg_ex, s):
    letters.add(r_item.group().lower())

print(len(letters))
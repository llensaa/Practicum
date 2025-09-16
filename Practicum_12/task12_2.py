'''
text = input()

if not text:
    print("0")
else:
    max_count = 1
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1

    print(max_count)
'''

from re import *

s = input()
reg_ex = r'(.)\1+'

m = 0
for r_item in finditer(reg_ex, s):
    m = max(m, len(r_item.group()))

print(m)
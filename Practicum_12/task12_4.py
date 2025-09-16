from re import *

s = input()
reg_ex = r'.'

counts = {}

for r_item in finditer(reg_ex, s):
    ch = r_item.group()   
    if ch not in counts:  
        counts[ch] = 0
    counts[ch] += 1     

for ch in counts:
    if counts[ch] == 3:
        print(ch)
        break
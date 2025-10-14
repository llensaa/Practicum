from re import *
import keyword

s = input()
reg_ex = r'[A-Za-z_][A-Za-z_0-9]*'

m = match(reg_ex, s)
if m and m.end() == len(s) and s not in keyword.kwlist:
    print('Может быть именем')
else:
    print('Не может быть именем')
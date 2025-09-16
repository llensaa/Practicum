from re import *

s1 = input()
s2 = input()
s3 = input()

reg_ex = r'.'

set1 = set(r_item.group() for r_item in finditer(reg_ex, s1))
set2 = set(r_item.group() for r_item in finditer(reg_ex, s2))
set3 = set(r_item.group() for r_item in finditer(reg_ex, s3))

result = (set1 ^ set2 ^ set3) - (set1 & set2 & set3)

print("".join(result))
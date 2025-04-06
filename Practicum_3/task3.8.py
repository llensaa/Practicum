import math as m

a = int(input())
b = int(input())
c = int(input())

cos_A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
cos_B = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
cos_C = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

A = m.degrees(m.acos(cos_A))
B = m.degrees(m.acos(cos_B))
C = m.degrees(m.acos(cos_C))

print(A, B, C, sep = '\n')
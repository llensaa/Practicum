from re import *

s = input()

while search(r'\([^()]+\)', s):
    s = sub(r'\(([^()]+)\)', lambda m: str(sum(map(int, m.group(1).split('+')))), s)

print(sum(map(int, s.split('+'))))

length_sm = float(input())
length_inch = length_sm / 2.54
length_foot = length_inch / 12
length_yard = length_foot / 3
length_mile = length_yard / 1760
print(str(length_yard) + ' в ярдах', str(length_mile) + ' в милях', str(length_foot) + ' в футах', str(length_inch) + ' в дюймах', sep = '\n')
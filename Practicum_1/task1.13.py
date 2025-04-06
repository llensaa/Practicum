import math
range_1 = int(input())
range_2 = int(input())
reception_range = max(range_1, range_2)
blind_spot_range = min(range_1, range_2)
area = (math.pi * reception_range ** 2) - (math.pi * blind_spot_range ** 2)
print(area)
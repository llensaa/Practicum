def find_smallest_sum_of_cubes():
    cubes = {}
    for a in range(1, 100):
        for b in range(a, 100):
            sum_of_cubes = a**3 + b**3
            if sum_of_cubes in cubes:
                cubes[sum_of_cubes].append((a, b))
            else:
                cubes[sum_of_cubes] = [(a, b)]
    for sum_of_cubes, pairs in cubes.items():
        if len(pairs) > 1:
            return sum_of_cubes, pairs

    return None

result = find_smallest_sum_of_cubes()
if result:
    print(f"Наименьшее число: {result[0]}")
    print("Способы представления:")
    for pair in result[1]:
        print(f"{pair[0]}^3 + {pair[1]}^3")
else:
    print("Не найдено такого числа.")

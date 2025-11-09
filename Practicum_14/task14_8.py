def line(elements):
    sorted_el = sorted(elements)
    line_el = " ".join(sorted_el)
    return line_el

elements = list(input().split())
print(line(elements))
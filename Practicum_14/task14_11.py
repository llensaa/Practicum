lst = list(map(int, input().split()))
command = input()

direction = command[0]
steps = int(command[1:])
n = len(lst)
effective_steps = steps % n

if direction == 'R':
    lst = lst[-effective_steps:] + lst[:-effective_steps]
elif direction == 'L':
    lst = lst[effective_steps:] + lst[:effective_steps]

print(*lst)
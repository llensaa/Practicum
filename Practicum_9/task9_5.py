def is_palindrome(s):
    return s == s[::-1]


for N in range(100000, 1000000):
    s = str(N)

    if not is_palindrome(s[1:]):
        continue

    s_plus_1 = str(N + 1)
    if len(s_plus_1) == 6 and not is_palindrome(s_plus_1[1:]):
        continue

    s_plus_2 = str(N + 2)
    if len(s_plus_2) == 6:
        middle_4 = s_plus_2[1:5]
        if not is_palindrome(middle_4):
            continue
    else:
        continue

    s_plus_3 = str(N + 3)
    if len(s_plus_3) == 6 and not is_palindrome(s_plus_3):
        continue

    print(N)
    break
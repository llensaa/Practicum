for i in range(10000, 99999):
    m = i // 10000
    o = i % 10000 // 1000
    n = i % 1000 // 100
    e = i % 100 // 10
    y = i % 10

    if len({m, o, n, e, y}) != 5:
        continue

    for s in range(1, 10):
        for d in range(1, 10):
            for r in range(1, 10):
                if (s == d or s == r or d == r or
                        s in {m, o, n, e, y} or
                        d in {m, o, n, e, y} or
                        r in {m, o, n, e, y}):
                    continue

                send = s * 1000 + e * 100 + n * 10 + d
                more = m * 1000 + o * 100 + r * 10 + e

                if send + more == i:
                    print(f"SEND = {send}, MORE = {more}, MONEY = {i}")
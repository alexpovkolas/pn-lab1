def merge(a, b):
    c = []
    idx_a = 0
    idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            c.append(a[idx_a])
            idx_a += 1
        else:
            c.append(b[idx_b])
            idx_b += 1

    c.extend(a[idx_a:])
    c.extend(b[idx_b:])

    return c if isinstance(a, list) else tuple(c)






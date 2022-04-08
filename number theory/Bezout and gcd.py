def bezout(a, b):
    s, t, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
    if a > 0:
        return [a, s, t]
    else:
        return [-a, -s, -t]
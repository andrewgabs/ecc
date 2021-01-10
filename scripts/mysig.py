import random

N = 337
G = 2477
Priv = 73
Pub = Priv * G

koaf = 1


def mul(a, b):
    return (a * b) % N


def div(a, b):
    return int(a / b) % N


def sign(z):
    r, s = 0, 0
    while not r or not s:
        global koaf
        koaf = random.randrange(1, N-1)
        print(f"K:{koaf}")
        r = koaf * G
        s = (z + Priv * r) / koaf
    return r, s


def ver(z, r, s):
    u1 = z / s
    u2 = r / s
    print(f"u1:{u1} u2:{u2}")
    P = int(u1 * G + u2 * Pub)
    print(f"P:{P}")
    assert koaf == r / G, r/G

    p1 = int(z * G / s + r * Priv * G / s)
    assert P == p1, p1

    p2 = int((z + r * Priv) / s * G)
    assert P == p2, p2

    p3 = int(koaf * G)
    assert P == p3, p3

    return P


hash = 1234343
r, s = sign(hash)
print(f"r/s: {r} : {s}")

p = ver(hash, r, s)
print(f"ver: {p}")
print(f"good: {p == r}")

import random

N = 337
G = 24777
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
        s = (z + Priv * r) // koaf

    assert s == z // koaf + Priv * G

    assert s == (z + Priv * koaf * G) // koaf

    assert s == z // koaf + Pub

    assert s - Pub == z // koaf

    assert koaf == z // ( s - Pub )

    return r, s


def ver(z, r, s):
    u1 = z / s
    u2 = r / s
    print(f"u1:{u1} u2:{u2}")
    assert koaf == r // G

    assert s - Pub == int(z * G / r)

    ####

    P = int(u1 * G + u2 * Pub)
    print(f"P:{P}")

    p1 = int(z * G / s + r * Pub / s)
    assert P == p1, p1

    p2 = (z + r * Priv) // s * G
    assert abs(P - p2) <= 3, p2
    assert r == (z + r * Priv) // s * G
    assert r / G == (z + r * Priv) // s
    assert r / G == (z + r * Priv) // (z // koaf + Pub)

    p3 = koaf * G
    assert p2 == p3, p3

    assert p2 == r

    return P


hash = 1234343
r, s = sign(hash)
print(f"r/s: {r} : {s}")

p = ver(hash, r, s)
print(f"ver: {p}")
print(f"good: {p == r}")

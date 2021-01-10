import random

N = 23
G = 103
Priv = 73
Pub = Priv * G


def sign(z):
    r, s = 0, 0
    while not r or not s:
        k = random.randrange(1, N-1)
        x = k * G
        r = x % N
        s = int((z + Priv * r) / k) % N
    return r, s


def ver(z, r, s):
    u1 = int(z / s) % N
    u2 = int(r / s) % N
    print(f"u1:{u1} u2:{u2}")
    P = u1 * G + u2 * Pub
    return P % N


hash = 123
r, s = sign(hash)
print(f"r/s: {r} : {s}")

p = ver(hash, r, s)
print(f"ver: {p}")

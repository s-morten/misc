import math

s = {
    7,
    12,
    17,
    22,
    7,
    12,
    17,
    22,
    7,
    12,
    17,
    22,
    7,
    12,
    17,
    22,
    5,
    9,
    14,
    20,
    5,
    9,
    14,
    20,
    5,
    9,
    14,
    20,
    5,
    9,
    14,
    20,
    4,
    11,
    16,
    23,
    4,
    11,
    16,
    23,
    4,
    11,
    16,
    23,
    4,
    11,
    16,
    23,
    6,
    10,
    15,
    21,
    6,
    10,
    15,
    21,
    6,
    10,
    15,
    21,
    6,
    10,
    15,
    21,
}

K = [[0] for x in range(64)]

for i in range(64):
    K[i] = math.floor(math.pow(2, 32) * abs(math.sin(i + 1)))
    print(K[i])

a0 = 0x67452301
b0 = 0xEFCDAB89
c0 = 0x98BADCFE
d0 = 0x10325476

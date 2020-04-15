from mpmath import mp
import math

mp.dps = 50
TEN = 10 ** 35
X = set()
for m in range(2, 10 ** 8):
    for k in range(2, 18 // int(math.log10(m) + 1) + 2):
        v = m ** (k * 2)
        if v > TEN:
            break
        X.add(v - 1)
s = mp.fsum([mp.fdiv(1, x) for x in X])
print('%.32f' % (mp.fsub(mp.fdiv(3, 4), s)))

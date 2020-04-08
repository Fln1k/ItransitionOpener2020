from math import *;from sympy.ntheory import *;from functools import *;from mpmath import *
def f(n):
	mp.dps=n;
	return(fsum(power(-~_*~-_,-1) for(_)in(range(2,n)) if(reduce(gcd,factorint(_).values())==1)))
counter = 40000
end = counter+2
previous = 0
while counter<end:
	now = f(counter)
	if int(previous*1000000000000000000000000000000) == int(now*1000000000000000000000000000000):
		break
	previous = now
	counter = counter + 1
print(f"answer = {int(previous*1000000000000000000000000000000)}")
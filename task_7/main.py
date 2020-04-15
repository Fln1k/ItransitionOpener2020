maxxx = 0

def dfs(n, k=1):
    global maxxx
    d = k - (16 * n) % (k + 1)
    if d < 0:
        d += k + 1
    x = format(n, 'x')
    if x[k // 2] == 'b' and k >= maxxx:
        maxxx = k
        print('k = ', k, 'x = ', format(n, 'x'), 'n = ', n)
    if d > 16:
        return
    while d < 16:
        dfs(16 * n + d, k + 1)
        d += k + 1


for i in range(1, 16):
    dfs(i)

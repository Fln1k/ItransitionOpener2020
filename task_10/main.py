def is_cube(n):
    root3 = round(n ** (1.0 / 3.0));
    return (n == root3 ** 3)


def is_sum_cubes(n):
    previous_n = 0
    previous_k = 0
    n_count = 0
    for k in range(1, n + 1):
        if is_cube(k) and n - k != 0 and is_cube(n - k):
            if n != previous_k and k != previous_n:
                previous_n = n - k
                previous_k = k
                n_count+=1
            if n_count == 2:
                print(n, " = ", k, " + ", n - k)
                return True
    return False


previous_flag = False
answer = None
for k in range(1000001):
    print(k)
    temp_flag = is_sum_cubes(k)
    if temp_flag and previous_flag:
        answer = k
        break
    previous_flag = temp_flag
print(answer)

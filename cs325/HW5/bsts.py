def bsts(n):
    if n == 0 or n == 1:
        return 1

    total = [0] * (n + 1)
    total[0] = 1
    total[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            total[i] += total[j] * total[i - j - 1]

    return total[n]

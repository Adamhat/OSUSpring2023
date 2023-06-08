import heapq

pairs = set(['AU', 'UA', 'GC', 'CG', 'GU', 'UG'])

def rna_seq(seq):
    n = len(seq)
    dp = [[0]*n for _ in range(n)]
    backtrack = [[None]*n for _ in range(n)]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            if seq[i:j+1] in pairs:
                dp[i][j] = dp[i+1][j-1] + 1
                backtrack[i][j] = (i+1, j-1)
            else:
                dp[i][j] = dp[i+1][j]
                backtrack[i][j] = (i+1, j)
                for k in range(i+1, j):
                    if dp[i][k] + dp[k+1][j] > dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k+1][j]
                        backtrack[i][j] = (i, k, k+1, j)
    return dp, backtrack

def recover(seq, backtrack, i, j):
    if i >= j:
        return '.' * (j - i + 1)
    if len(backtrack[i][j]) == 2:
        return '(' + recover(seq, backtrack, *backtrack[i][j]) + ')'
    else:
        a, b, c, d = backtrack[i][j]
        return recover(seq, backtrack, a, b) + recover(seq, backtrack, c, d)

def best(seq):
    dp, backtrack = rna_seq(seq)
    i, j = 0, len(seq) - 1
    return dp[i][j], recover(seq, backtrack, i, j)

def total(seq):
    n = len(seq)
    dp = [[0]*n for _ in range(n)]
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            if seq[i:j+1] in pairs:
                dp[i][j] = dp[i+1][j-1] + 1
            for k in range(i, j):
                dp[i][j] += dp[i][k] * dp[k+1][j]
    return dp[0][n-1]

def kbest(seq, k):
    dp, backtrack = rna_seq(seq)
    n = len(seq)
    heap = [(-dp[0][n-1], 0, n-1, recover(seq, backtrack, 0, n-1))]
    result = []
    while heap and len(result) < k:
        _, i, j, structure = heapq.heappop(heap)
        if structure not in result:
            result.append((dp[i][j], structure))
        if i < j:
            if len(backtrack[i][j]) == 2:
                x, y = backtrack[i][j]
                heapq.heappush(heap, (-dp[x][y], x, y, recover(seq, backtrack, x, y)))
            else:
                a, b, c, d = backtrack[i][j]
                heapq.heappush(heap, (-dp[a][b], a, b, recover(seq, backtrack, a, b)))
                heapq.heappush(heap, (-dp[c][d], c, d, recover(seq, backtrack, c, d)))
    return result

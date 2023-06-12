def populate_dp_and_counts(seq, valid_pairs, dp, counts):
    n = len(seq)
    for gap in range(2, n+1):
        for i in range(n-gap+1):
            j = i+gap-1
            if seq[i] + seq[j] in valid_pairs:
                counts[i][j] = counts[i+1][j-1] + 1
            for k in range(i, j):
                counts[i][j] = max(counts[i][j], counts[i][k] + counts[k+1][j])

def get_structure(seq, valid_pairs, dp, counts, i, j):
    if i >= j:
        return '.' * (j - i + 1)
    if dp[i][j]:
        return dp[i][j]
    max_count = counts[i][j]
    if seq[i] + seq[j] in valid_pairs and counts[i+1][j-1] + 1 == max_count:
        dp[i][j] = '(' + get_structure(seq, valid_pairs, dp, counts, i+1, j-1) + ')'
    else:
        for k in range(i, j):
            if counts[i][k] + counts[k+1][j] == max_count:
                dp[i][j] = get_structure(seq, valid_pairs, dp, counts, i, k) + get_structure(seq, valid_pairs, dp, counts, k+1, j)
                break
    return dp[i][j]

def best(seq):
    valid_pairs = {'AU', 'UA', 'CG', 'GC', 'GU', 'UG'}
    n = len(seq)
    dp = [['']*n for _ in range(n)]
    counts = [[0]*n for _ in range(n)]

    populate_dp_and_counts(seq, valid_pairs, dp, counts)
    
    return counts[0][n-1], get_structure(seq, valid_pairs, dp, counts, 0, n-1)


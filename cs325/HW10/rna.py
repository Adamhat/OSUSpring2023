import heapq

pairs = set(['AU', 'UA', 'GC', 'CG', 'GU', 'UG'])

def rna_seq(seq):
    n = len(seq)
    rna = [[0] * n for _ in range(n)]
    backtrack = [[None] * n for _ in range(n)]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            if seq[i] + seq[j] in pairs and rna[i + 1][j - 1] + 1 > rna[i][j]:
                rna[i][j] = rna[i + 1][j - 1] + 1
                backtrack[i][j] = (i + 1, j - 1)
            for k in range(i + 1, j):
                if rna[i][k] + rna[k + 1][j] > rna[i][j]:
                    rna[i][j] = rna[i][k] + rna[k + 1][j]
                    backtrack[i][j] = (i, k, k + 1, j)

    return rna, backtrack

def reconstruct(seq, backtrack, i, j):
    if i >= j:
        return '.' * (j - i + 1)
    elif backtrack[i][j] is not None and len(backtrack[i][j]) == 2:
        x, y = backtrack[i][j]
        return '(' + reconstruct(seq, backtrack, x, y) + ')'
    elif backtrack[i][j] is not None and len(backtrack[i][j]) == 4:
        a, b, c, d = backtrack[i][j]
        return reconstruct(seq, backtrack, a, b) + reconstruct(seq, backtrack, c, d)
    else:
        return '.' * (j - i + 1)

def best(seq):
    rna, backtrack = rna_seq(seq)
    i, j = 0, len(seq) - 1
    return rna[i][j], reconstruct(seq, backtrack, i, j)

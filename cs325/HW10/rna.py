def helper(sequence, valid_pairs, dp_table, count):
    n = len(sequence)
    for x in range(2, n + 1):
        for i in range(n - x + 1):
            j = i + x - 1
            if sequence[i] + sequence[j] in valid_pairs:
                count[i][j] = count[i + 1][j - 1] + 1
            for k in range(i, j):
                count[i][j] = max(count[i][j], count[i][k] + count[k + 1][j])

def get_structure(sequence, valid_pairs, dp_table, count, i, j):
    if i >= j:
        return '.' * (j - i + 1)
    if dp_table[i][j]:
        return dp_table[i][j]
    max = count[i][j]
    if sequence[i] + sequence[j] in valid_pairs and count[i + 1][j - 1] + 1 == max:
        dp_table[i][j] = '(' + get_structure(sequence, valid_pairs, dp_table, count, i + 1, j - 1) + ')'
    else:
        for k in range(i, j):
            if count[i][k] + count[k+1][j] == max:
                dp_table[i][j] = get_structure(sequence, valid_pairs, dp_table, count, i, k) + get_structure(sequence, valid_pairs, dp_table, count, k + 1, j)
                break
    return dp_table[i][j]

def best(sequence):
    valid_pairs = {'AU', 'UA', 'CG', 'GC', 'GU', 'UG'}
    n = len(sequence)
    dp_table = [[''] * n for _ in range(n)]
    count = [[0] * n for _ in range(n)]

    helper(sequence, valid_pairs, dp_table, count)
    
    return count[0][n - 1], get_structure(sequence, valid_pairs, dp_table, count, 0, n - 1)

def kbest(sequence, k):
    valid_pairs = {'AU', 'UA', 'CG', 'GC', 'GU', 'UG'}
    n = len(sequence)
    dp_table = [[None] * n for _ in range(n)]
    counts = [[0] * n for _ in range(n)]
    helper(sequence, valid_pairs, dp_table, counts)
    return get_k_structure(sequence, valid_pairs, dp_table, counts, 0, n - 1, k)[:k]

def get_k_structure(sequence, valid_pairs, dp_table, counts, i, j, k):
    if i >= j:
        return [(0, '.' * (j - i + 1))]
    if dp_table[i][j] is not None:
        return dp_table[i][j][:k]
    possibilities = []
    if sequence[i] + sequence[j] in valid_pairs:
        for structure in get_k_structure(sequence, valid_pairs, dp_table, counts, i + 1, j - 1, k):
            possibilities.append((structure[0] + 1, '(' + structure[1] + ')'))
    for mid in range(i, j):
        for left in get_k_structure(sequence, valid_pairs, dp_table, counts, i, mid, k):
            for right in get_k_structure(sequence, valid_pairs, dp_table, counts, mid + 1, j, k):
                possibilities.append((left[0] + right[0], left[1] + right[1]))
    dp_table[i][j] = sorted(set(possibilities), reverse=True)
    return dp_table[i][j][:k]

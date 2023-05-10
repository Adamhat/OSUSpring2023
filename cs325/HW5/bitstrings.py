def num_no(n):
    endsZero = [0]*(n + 1)
    endsOne = [0]*(n + 1)
    endsZero[1] = endsOne[1] = 1
    
    for i in range(2, n + 1):
        endsZero[i] = endsOne[i - 1]
        endsOne[i] = endsZero[i - 1] + endsOne[i-1]
    
    return endsZero[n] + endsOne[n]

def num_yes(n):
    return 2**n - num_no(n)

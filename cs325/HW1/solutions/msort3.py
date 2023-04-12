#!/usr/bin/env python3

__author__ = "Liang Huang" # O(nlogn) version 1: appending

def mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

def mergesorted(a, b):
    if a == [] or b == []:
        return a+b
    c = []
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la and j < lb: # both non-empty
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    # at least one of them is empty
    c += a[i:] + b[j:]
    return c

if __name__ == "__main__":
    import sys, time
    import random
    random.seed(0)
    sys.setrecursionlimit(100000)
    n = 1000
    while n <= 128000:
        a = random.sample(list(range(n)), n) # random permutation
        t = time.time()
        b = mergesort(a)
        print(sorted(a) == b)
        print(n, time.time() - t)
        n *= 2

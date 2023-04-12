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
    while a != [] and b != []: # both non-empty
        if a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    # at least one of them is empty
    c += a + b
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

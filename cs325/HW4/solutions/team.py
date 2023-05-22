#!/usr/bin/env python3

__author__ = "Liang Huang"

from heapq import heapify, heapreplace

def _select(*lists): # my code, not as elegant as Otso's
    k = len(lists)
    n = len(lists[0])
    heap = [(a[0], i, 0) for i, a in enumerate(lists)]
    heapify(heap)
    for _ in range(n):
        x, i, j = heap[0]
        yield x
        if j < n-1:
            heapreplace(heap, (lists[i][j+1], i, j+1))

def _select2(*lists): # Otso Barron's more elegant version
    k = len(lists)
    n = len(lists[0])
    heap = [(a[0], a, 0) for a in lists] # no need for index i
    heapify(heap)
    for _ in range(n):
        x, a, j = heap[0]
        yield x
        if j < n-1:
            heapreplace(heap, (a[j+1], a, j+1))

select = lambda *x: list(_select2(*x))

if __name__ == "__main__":
    from random import randint
    import sys
    try:
        k, n = list(map(int, sys.argv[1:3]))
    except:
        k, n = 10, 5
    lists = [sorted([randint(0, 200) for _ in range(n)]) for _ in range(k)]
    print(lists)
    print(select(*lists))

    # check with naive solution
    flatten = sum(lists, []) # 2nd argument is the base value, default 0
    print(sorted(flatten)[:n])

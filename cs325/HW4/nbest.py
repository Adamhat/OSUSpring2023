from random import randint
import heapq

def qselect(k, a):
    index = randint(0, len(a) - 1)
    a[0], a[index] = a[index], a[0]
    pivot = a[0]

    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    leftSize = len(left) + 1
    if k == leftSize:
        return pivot
    return qselect(k, left) if k < leftSize else qselect(k - leftSize, right)

def helperOne(pair):
    return pair[0] + pair[1], pair[1]

def nbesta(a, b):
    pairs = [(x, y) for x in a for y in b]
    pairs.sort(key=helperOne)
    return pairs[:len(a)]

def nbestb(a, b):
    pairs = [(x, y) for x in a for y in b]
    sortedPairs = sorted(pairs, key=helperOne)
    return [pair for i, pair in enumerate(sortedPairs) if i < len(a)]

def nbestc(a, b):
    minHeap = []
    for x in a:
        for y in b:
            heapq.heappush(minHeap, ((x + y, y), (x, y)))
            if len(minHeap) > len(a) * 2:
                heapq.heappop(minHeap)
    return sorted([pair for z, pair in minHeap], key=helperOne)[:len(a)]

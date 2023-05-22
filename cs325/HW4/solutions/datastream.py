#!/usr/bin/python3

import heapq

def ksmallest(k, l): # slow
    if k == 0: return []
    heap = []
    for i, x in enumerate(l):
        if i < k:
            heapq.heappush(heap, -x)
        elif -x > heap[0]:
            heapq.heapreplace(heap, -x)
    return sorted([-x for x in heap])

def ksmallest2(k, l): # a bit faster than the above
    if k == 0: return []
    l = iter(l) # iterator, so you can call next()
    heap = []
    for _ in range(k): # k << n, so no need to try ... except
        heap.append(-next(l))
    heapq.heapify(heap)
    for x in l:
        if -x > heap[0]:
            heapq.heapreplace(heap, -x)
    return sorted([-x for x in heap])
    
if __name__=="__main__":        
    import random

    print(ksmallest(20, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(ksmallest(3, range(1000000, 0, -1)))

    l = [random.randint(0,100) for r in range(200)]
    print(ksmallest(6,l))
    # check with naive solution
    print(sorted(l)[:6])

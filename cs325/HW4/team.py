import heapq

def select(*a):
    heap = []
    result = []
    n = len(a[0])

    for index, lst in enumerate(a):
        heapq.heappush(heap, (lst[0], index, 0))
    for x in range(n):
        value, index, position = heapq.heappop(heap)
        result.append(value)
        if position + 1 < len(a[index]):
            heapq.heappush(heap, (a[index][position + 1], index, position + 1))

    return result

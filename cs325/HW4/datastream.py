import heapq

def ksmallest(k, arr):
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        else:
            if -num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)
    return sorted([-x for x in heap])

# if __name__ == "__main__":
#     print(ksmallest(5, (x**2 for x in range(10,0,-1))))
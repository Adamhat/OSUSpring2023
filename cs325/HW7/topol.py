def order(n, list_of_edges):
    list = [[] for _ in range(n)]
    for x, y in list_of_edges:
        list[x].append(y)

    searched = [False]*n
    searching = [False]*n
    solution = []

    def depth_search(point):
        if searched[point]:
            return True
        if searching[point]:
            return False

        searching[point] = True

        for z in list[point]:
            if not depth_search(z):
                return False

        searching[point] = False
        searched[point] = True

        solution.append(point)

        return True

    for point in range(n):
        if not searched[point]:
            if not depth_search(point):
                return None
    return solution[::-1]


print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])) # [0, 1, 2, 3, 4, 5, 6, 7]
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])) # [0, 1, 2, 4, 3, 5, 6, 7]
print(order(4, [(0,1), (1,2), (2,1), (2,3)])) # None
print(order(5, [(0,1), (1,2), (2,3), (3,4)])) # [0, 1, 2, 3, 4]
print(order(5, [])) # [0, 1, 2, 3, 4]
print(order(3, [(1,2), (2,1)])) # None
print(order(1, [(0,0)])) # None
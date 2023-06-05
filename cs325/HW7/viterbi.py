def longest(n, list_of_edges):
    list = [[] for _ in range(n)]
    for x, y in list_of_edges:
        list[x].append(y)

    searched = [False]*n
    order = []

    def depth_search(point):
        searched[point] = True
        for z in list[point]:
            if not searched[z]:
                depth_search(z)
        order.append(point)

    for point in range(n):
        if not searched[point]:
            depth_search(point)
    order = order[::-1]

    longest_path = [0]*n
    traceback = [-1]*n
    for point in order:
        for z in list[point]:
            if longest_path[point] + 1 > longest_path[z]:
                longest_path[z] = longest_path[point] + 1
                traceback[z] = point

    end = longest_path.index(max(longest_path))
    path = []
    while end != -1:
        path.append(end)
        end = traceback[end]
    path = path[::-1]

    return max(longest_path), path

from pqdict import pqdict

def shortest(n, edges):
    graph = {}
    
    for i in range(n):
        graph[i] = {}
        
    for x, y, z in edges:
        graph[x][y] = z
        graph[y][x] = z

    prio_queue = pqdict()
    shortest_dictionary = {}
    for i in range(n):
        prio_queue[i] = float('inf')
        
    prio_queue[0] = 0
    
    line = {}
    for i in range(n):
        line[i] = []
        
    line[0] = [0]

    while prio_queue:
        x, shortest_to_x = prio_queue.popitem()

        for y, length_x_y in graph[x].items():
            if y in prio_queue:
                hold = shortest_to_x + length_x_y
                if hold < prio_queue[y]:
                    prio_queue[y] = hold
                    shortest_dictionary[y] = hold
                    line[y] = line[x] + [y]

    if not line[n-1]:
        return None

    return shortest_dictionary[n-1], line[n-1]

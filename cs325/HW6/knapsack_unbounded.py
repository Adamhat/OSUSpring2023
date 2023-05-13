def best(W, items):
    n = len(items)
    maxValue = [0 for x in range(W + 1)]
    choice = [0 for y in range(W + 1)]
    total = [0 for z in range(n)]

    for i, (weight, value) in enumerate(items):
        for w in range(weight, W + 1):
            if maxValue[w] < maxValue[w - weight] + value:
                maxValue[w] = maxValue[w - weight] + value
                choice[w] = i
                
    w = W
    while w > 0:
        total[choice[w]] += 1
        w -= items[choice[w]][0]

    return maxValue[W], total

def best(W, items):
    n = len(items)
    maxValue = [0 for x in range(W + 1)]
    choice = [[0]*n for y in range(W + 1)]
    
    for i, (weight, value, count) in enumerate(items):
        for w in range(W, weight - 1, -1):  
            for c in range(1, min(w//weight, count) + 1):
                if maxValue[w] < maxValue[w - c * weight] + c * value:
                    maxValue[w] = maxValue[w - c * weight] + c * value
                    choice[w] = choice[w - c * weight][:]
                    choice[w][i] += c
    
    return maxValue[W], choice[W]

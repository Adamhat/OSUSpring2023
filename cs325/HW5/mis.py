def max_wis(arr):
    if not arr:
        return 0, []

    sum = [0] * (len(arr) + 1)
    independentSet = [[] for x in range(len(arr) + 1)]

    for i in range(1, len(arr) + 1):
        sumWithElement = sum[i - 2] + arr[i - 1]
        sumWithoutElement = sum[i - 1]

        if sumWithElement > sumWithoutElement:
            sum[i] = sumWithElement 
            independentSet[i] = independentSet[i - 2] + [arr[i - 1]]
        else:
            sum[i] = sumWithoutElement
            independentSet[i] = independentSet[i - 1]

    return sum[-1] if sum[-1] > 0 else 0, independentSet[-1]
    
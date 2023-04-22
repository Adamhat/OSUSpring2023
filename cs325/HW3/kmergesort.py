def kmergesort(arr, k):
    if len(arr) <= 1:
        return arr
    
    if k <= 1:
        k = 2

    arrSize = (len(arr) + k - 1) // k
    
    split = []
    for i in range(0, len(arr), arrSize):
        split.append(arr[i:i+arrSize])

    for i in range(len(split)):
        split[i] = kmergesort(split[i], k)

    result = []
    while any(split):
        smallest = min([x[0] for x in split if x], default=None)
        if smallest is None:
            break
        for i, x in enumerate(split):
            if x and x[0] == smallest:
                result.append(x.pop(0))

    return result

#if __name__ == "__main__":
#    print(kmergesort([4,1,5,2,6,3,7,0], 1))

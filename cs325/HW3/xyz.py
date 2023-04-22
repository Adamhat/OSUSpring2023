def find(arr):
    arr.sort()
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            z = arr[i] + arr[j]
            if z in arr[j+1:]:
                print(arr[j+1:])
                result.append((arr[i], arr[j], z))
    return result

#if __name__ == "__main__":
#    print(find([1, 4, 2, 3, 5]))


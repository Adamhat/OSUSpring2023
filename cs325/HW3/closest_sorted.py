import bisect

def find(arr, x, k):
    index = bisect.bisect_left(arr, x)
    print(index)
    left = index - 1
    right = index
    while right - left <= k:
        if left == -1:
            return arr[:k]
        elif right == len(arr):
            return arr[-k:]
        elif x - arr[left] <= arr[right] - x:
            left -= 1
        else:
            right += 1
    return arr[left+1:right]
        

#if __name__ == "__main__":
#    print(find([1,2,3,4,4,7], 5.2, 2))
#    print(find([1,2,3,4,4,7], 6.5, 3))
#    print(find([1,2,3,4,4,6,6], 5, 3))
#    print(find([1,2,3,4,4,5,6], 4, 5))

def qselect(lowestValue, arr):
    if arr == []:
        return []
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        i = len(left) + 1 # Pivot is always located +1 to the length of the left sub array
        if lowestValue < i:
            return qselect(lowestValue, left)
        elif lowestValue == i:
            return pivot
        else:
            return qselect(lowestValue - i, right)

if __name__ == '__main__':
    print(qselect(2, [3, 10, 4, 7, 19]))
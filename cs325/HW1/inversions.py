def num_inversions(arr):
    total = 0
    if len(arr) > 1:
        leftArray = arr[:len(arr)//2] # From beginning to mid of original array. :len is the same as 0:len.
        rightArray = arr[len(arr)//2:] # From mid (len(arr)//2) to end of original array. Double slash // rounds value. //2: is the same as //2:len(arr)
        
        total += num_inversions(leftArray) # Recursively call mergesort function on both sides. Gives two arrays in sorted order.
        total += num_inversions(rightArray) 
        
        i, j, k = 0, 0, 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
                total += len(leftArray) - i # If the left array value is greater then the right array value we know there is an inversion.
            k += 1
        
        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1
            
        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1
    return total

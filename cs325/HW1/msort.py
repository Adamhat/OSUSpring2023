def mergesort(arr):
    if len(arr) > 1:
        leftArray = arr[:len(arr)//2] # From beginning to mid of original array. :len is the same as 0:len.
        rightArray = arr[len(arr)//2:] # From mid (len(arr)//2) to end of original array. Double slash // rounds value. //2: is the same as //2:len(arr)
        
        mergesort(leftArray) # Recursively call mergesort function on both sides. Gives two arrays in sorted order.
        mergesort(rightArray) 
        
        i, j, k = 0, 0, 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1
        
        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1
            
        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1
    return arr

from random import randint

def qselect(k, a):
    index = randint(0, len(a)-1) # randomized pivot position
    a[0], a[index] = a[index] , a[0] # swap pivot with a[0]
    pivot = a[0]
        
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    left_size = len(left)+1 # including pivot
    if k == left_size:
        return pivot
    return qselect(k, left) if k < left_size else qselect(k - left_size, right)

print(qselect(1, [3,2,54,1]))
print(qselect(4, [11, 2, 8, 3]))

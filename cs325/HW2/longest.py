def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]
    
def longest(tree):
    return 0

if __name__ == "__main__":
    tree = sort([3, 1, 2])
    print(tree)
    longest(tree)
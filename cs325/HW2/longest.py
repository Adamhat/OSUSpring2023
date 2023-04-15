def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]
    
def height(tree):
    if tree == []:
        return 0
    else:
        leftHeight = height(tree[0])
        rightHeight = height(tree[2])
        return max(leftHeight, rightHeight) + 1
    
def longest(tree):
    if tree == []:
        return 0
    else:
        leftHeight = height(tree[0])
        rightHeight = height(tree[2])
        return max(leftHeight + rightHeight, max(longest(tree[0]), longest(tree[2])))
    

#if __name__ == "__main__":
#    tree = [[], 1, []]
#    print(longest(tree))
#    
#    tree = [[[], 1, []], 2, [[], 3, []]]
#    print(longest(tree))
#    
#    tree = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
#    print(longest(tree))
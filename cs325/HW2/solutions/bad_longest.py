# this code does NOT use recursion with byproduct
# instead, it calls depth() at every node
# as a result, it runs in worst-case O(n^2) time -- think about linear-chain tree

# Testing Case  1 (open)...0.000 s, Correct
# Testing Case  2 (open)...0.000 s, Correct
# Testing Case  3 (open)...0.000 s, Correct
# Testing Case  4 (open)...0.000 s, Correct
# Testing Case  5 (open)...0.001 s, Correct
# Testing Case  6 (hidden)...0.003 s, Correct
# Testing Case  7 (hidden)...0.014 s, Correct
# Testing Case  8 (hidden)...0.031 s, Correct
# Testing Case  9 (hidden)...0.403 s, Time Limit Exceeded
# Testing Case 10 (hidden)...0.403 s, Time Limit Exceeded

def longest(tree):
    if tree == []:
        return 0
    
    left, root, right = tree

    #Get left and right depth
    leftDepth = _depth(left)
    rightDepth = _depth(right)

    #Check subtree lengths
    leftLength = longest(left)
    rightLength = longest(right)

    #Either keep length passing through root, or keep larger length going through root of left/right subtree.
    # if leftDepth + rightDepth > max(leftLength, rightLength):
    #     return leftDepth + rightDepth
    # else:
    #     return max(leftLength, rightLength)
    return max(leftDepth + rightDepth, max(leftLength, rightLength)) 

#Calculate the depth of a tree from a root
def _depth(tree):
    if tree == []:
        return 0

    left, root, right = tree

    #Traverse tree 
    rightCount = _depth(right)
    leftCount = _depth(left)

    #Return larger subtree depth count
    if(leftCount > rightCount):
        return leftCount + 1
    else:
        return rightCount + 1 


#Debugging function to print tree
def pp(tree, dep = 0):
    if tree == []:
        return
    left, root, right = tree
    pp(left, dep + 1)
    print(" |" * dep, root)
    pp(right, dep + 1)

# Test code
# print(longest([[], 1, []]))
# print(longest([[[], 1, []], 2, [[], 3, []]]))
# print(longest([[[[[[], 0, []], 1, [[[], 2, []], 3, []]], 4, [[[[[], 5, []], 6, []], 7, []], 8, []]], 9, [[], 10, []]], 11, []]))
# pp([[[[[[], 0, []], 1, [[[], 2, []], 3, []]], 4, [[[[[], 5, []], 6, []], 7, []], 8, []]], 9, [[], 10, []]], 11, []])

def _longest(tree): # returns (height, max-path-length); here height is # of nodes (i.e., # of edges +1)
    if tree == []:
        return 0, 0
    dep_left, max_left = _longest(tree[0])
    dep_right, max_right = _longest(tree[2])
    return max(dep_left, dep_right) + 1, max(max_left, max_right, dep_left + dep_right) # no need to +2 here

longest = lambda tree: _longest(tree)[1]

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[],1,[]], 2, [[],3,[]]]))

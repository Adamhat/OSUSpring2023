def _longest(tree): # returns (height, max-path-length); here heigth is number of edges
    if tree == []:
        return -1, 0 # faithful to the lecture videos
    dep_left, max_left = _longest(tree[0])
    dep_right, max_right = _longest(tree[2])
    return max(dep_left, dep_right) + 1, max(max_left, max_right, dep_left + dep_right + 2) # here +2

longest = lambda tree: _longest(tree)[1]

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[],1,[]], 2, [[],3,[]]]))

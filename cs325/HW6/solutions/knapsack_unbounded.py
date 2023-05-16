#!/usr/bin/env python3

from collections import defaultdict

# O(nW) time; O(W) space
def best(W, items): # top-down
    back = defaultdict(lambda : None)
    
    def _best(x, opt=defaultdict(int)):
        if x in opt:
            return opt[x]
        print("solving", x)
        for i, (w, v) in enumerate(items):
            if x >= w:
                ans = _best(x-w) + v
                if ans > opt[x]:
                    opt[x] = ans
                    back[x] = i
        print("best:", x, opt[x], back[x])
        return opt[x]

    #print("# of subproblems solved:", len(back))
    return _best(W), solution(W, back, items)

def solution(x, back, items):
    i = back[x]
    #print("starting at", x, "let's take item", i)
    if i is None: # base case
        return [0] * len(items)
    w, _ = items[i]
    a = solution(x-w, back, items)
    a[i] += 1
    #print("finishing at", x, "after taking item", i, items[i], a)
    return a

def best2(W, items): # bottom-up
    back = defaultdict(lambda : None)
    opt = defaultdict(int)

    for x in range(1, W+1):
        for i, (w, v) in enumerate(items):
            if x >= w:
                ans = opt[x-w] + v
                if ans > opt[x]:
                    opt[x] = ans
                    back[x] = i
                    
    return opt[W], solution(W, back, items)

if __name__ == "__main__":

    print(best(3, [(2, 4), (3, 5)]))
    print(best(3, [(1, 5), (1, 5)]))
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))

    print(best2(3, [(2, 4), (3, 5)]))
    print(best2(3, [(1, 5), (1, 5)]))
    print(best2(3, [(1, 2), (1, 5)]))
    print(best2(3, [(1, 2), (2, 5)]))

#!/usr/bin/env python3

'''based on Rachel (sousar)'s code; minor edits by the instructor.'''

from collections import defaultdict

def best1(W, a):

    def solution(i, w):
        if i < 0:
            return []
        num_copies = back[w][i]
        weight, _, _ = a[i]
        return solution(i-1, w - weight * num_copies).__iadd__([num_copies]) # O(1) __iadd__

    dp = defaultdict(lambda: defaultdict(int)) 
    back = defaultdict(lambda: defaultdict(int)) 

    for i, (weight, value, count) in enumerate(a): # 0-based in dp/back
        for w in range(1, W+1):
            for j in range(min(count, w//weight)+1):
                v = dp[w - j*weight][i-1] + j*value
                if v > dp[w][i]:
                    dp[w][i] = v
                    back[w][i] = j
    return dp[W][len(a)-1], solution(len(a)-1, W)

def best(W, a):

    def solution(i, w):
        if i < 0:
            return []
        num_copies = back[w][i]
        weight, _, _ = a[i]
        return solution(i-1, w - weight * num_copies).__iadd__([num_copies]) # O(1) __iadd__

    dp = [[None] * len(a) for _ in range(W+1)] #defaultdict(lambda: defaultdict(lambda : None)) 
    back = [[0] * len(a) for _ in range(W+1)] #defaultdict(lambda: defaultdict(int)) 

    def _best2(w, i):
        if w <= 0 or i < 0:
            return 0
        if dp[w][i] is None:
            dp[w][i] = 0
            weight, value, count = a[i]
            for j in range(min(count, w//weight)+1):
                v = _best2(w - j*weight, i-1) + j*value
                if v > dp[w][i]:
                    dp[w][i] = v
                    back[w][i] = j

            #print(w, i, dp[w][i], back[w][i])

        return dp[w][i]

    tmp = _best2(W, len(a)-1)
    #print(dp)
    return tmp, solution(len(a)-1, W)

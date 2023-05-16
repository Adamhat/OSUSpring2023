# max_wis and max_wis2 are O(n) time & space (required)
# max_wis3 is O(n) time and O(1) space (not required)
# max_wis4 is O(n^2) time & space (BAD!)

def max_wis(a): # top-down; required
    best = {-1:0, -2:0} # 0-based index
    back = {}
    n = len(a)

    def top_down(i):
        if i not in best:
            best[i] = max(top_down(i-1), top_down(i-2)+a[i])
            back[i] = best[i] == best[i-1] # True if NOT take a[i]
        return best[i]

    return top_down(n-1), solution(n-1, a, back)

def solution(i, a, back): # recursive backtracing; shared by max_wis and max_wis2; BAD: O(n^2)-time
    if i < 0:
        return []
    return solution(i-1, a, back) if back[i] else (solution(i-2, a, back) + [a[i]]) # BAD: O(n) for this +!

def max_wis2(a): # bottom-up; required
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        back[i] = best[i] == best[i-1] # True if not take i
    return best[n-1], solution(n-1, a, back)

def myappend(a, x):
    a.append(x)
    return a

def solutionb(i, a, back): # recursive backtracing; O(n)-time
    if i < 0:
        return []
    return solutionb(i-1, a, back) if back[i] else solutionb(i-2, a, back).__iadd__([a[i]]) # O(1) for __iadd__
    #return solutionb(i-1, a, back) if back[i] else myappend(solutionb(i-2, a, back),a[i]) # also O(1)

def solutionc(a, back): # non-recursive backtracing (Otso Barron's style); fastest
    sol = []
    i = len(a)-1
    while i >= 0: # for-loop doesn't work
        if not back[i]:
            sol.append(a[i])
            i -= 1
        i -= 1            
    return sol[::-1] # reverse the order!

def max_wis2b(a): # bottom-up; required
    best = {-1: 0, -2: 0}
    back = {}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        back[i] = best[i] == best[i-1] # True if not take i
    return best[n-1], solutionc(a, back) #solutionb(n-1, a, back)


def max_wis3(a): # O(1)-space, O(n) time; with binary number (bit operations) for back; not required
    x, y = 0, 0
    back = 0
    n = len(a)
    for i in range(n):
        x, y = y, max(y, x+a[i]) # like Fibonacci (see fib.py)
        back = back << 1 | (x == y)     # or back = back * 2 + (x==y)
    return y, solution3(n-1, a, back)

def solution3(i, a, back): # backtracing for max_wis3; not required
    if i < 0:
        return []
    return solution3(i-1, a, back >> 1) if back & 1 else (solution3(i-2, a, back >> 2) + [a[i]]) # or back%2; note back>>2!

def max_wis4(a): # BAD: storing subsolutions slows it down to O(n^2)
    best = {-1: 0, -2: 0}
    path = {-1: [], -2: []}
    n = len(a)
    for i in range(n):
        best[i] = max(best[i-1], best[i-2]+a[i]) 
        path[i] = path[i-1] if best[i] == best[i-1] else path[i-2] + [a[i]]
    return best[n-1], path[n-1]

if __name__ == "__main__":

    import sys, random
    sys.setrecursionlimit(1000000)

    example = [9, 10, 8, 5, 2, 4]
    print(max_wis2(example))
    print(max_wis2b(example))

    #lst = [random.randint(-1e5,1e5) for _ in range(20000)]

    from time import time
    for n in [100, 1000, 10000, 20000, 40000]: #, 10000000, 100000000]:
        t = time()
        a = [random.randint(-1e5,1e5) for _ in range(n)]
        sol = max_wis2(a)
        atime = time() - t

        t = time()
        sol2 = max_wis2b(a)
        print(n, atime, time() - t, sol[1] == sol2[1])
        
    # t = time()
    # a = max_wis(lst)
    # print("max_wis : top-down\t", time() -t) 
    # t = time()
    # b = max_wis2(lst)
    # print("max_wis2: bottom-up\t", time() -t) 
    # t = time()
    # c = max_wis3(lst)
    # print("max_wis3: bit oper.\t", time() -t) 
    # t = time()
    # d = max_wis4(lst)
    # print("max_wis4: slow (subsol)\t", time() - t)
    # print(a == b == c == d) # verify result
    # #print(a==b)


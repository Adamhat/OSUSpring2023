def _search(t, x):
    for i in t:
        if isinstance(i, list):
            subTree = _search(i, x)
            if subTree is not None:
                return subTree
        elif i == x:
            return t
    return None

def search(t, x):
    inArray = _search(t, x)
    if inArray == None:
        return False
    return True

def sorted(t):
    sortedList = []
    for i in t:
        if isinstance(i, list):
            subList = sorted(i)
            sortedList = sortedList + subList
        else:
            sortedList.append(i)
    return sortedList
            

def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]
    
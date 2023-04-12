from qsort import insert, search, sort, sorted

if __name__ == "__main__":
    arr = [6, 0, 4, 3, 9, 7]
    print("Testing Buggy Qsort on initial array:", arr)
    tree = sort(arr)

    try:
        # 1
        print("Search 9:", "Passed" if search(tree, 9) else "Failed")
        insert(tree, 9)
        print("Insert 9:", "Passed" if sorted(tree) == [0, 3, 4, 6, 7, 9] else "Failed")
        print("Search 9:", "Passed" if search(tree, 9) else "Failed")

        # 2
        print("Search 8:", "Passed" if not search(tree, 8) else "Failed")
        insert(tree, 8)
        print("Insert 8:", "Passed" if sorted(tree) == [0, 3, 4, 6, 7, 8, 9] else "Failed")
        print("Search 8:", "Passed" if search(tree, 8) else "Failed")

        # 3
        print("Search 2:", "Passed" if not search(tree, 2) else "Failed")
        insert(tree, 2)
        print("Insert 2:", "Passed" if sorted(tree) == [0, 2, 3, 4, 6, 7, 8, 9] else "Failed")
        print("Search 2:", "Passed" if search(tree, 2) else "Failed")

        # 4
        print("Search 5:", "Passed" if not search(tree, 5) else "Failed")
        insert(tree, 5)
        print("Insert 5:", "Passed" if sorted(tree) == [0, 2, 3, 4, 5, 6, 7, 8, 9] else "Failed")
        print("Search 5:", "Passed" if search(tree, 5) else "Failed")

        # 5
        print("Search 1:", "Passed" if not search(tree, 1) else "Failed")
        insert(tree, 1)
        print("Insert 1:", "Passed" if sorted(tree) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] else "Failed")
        print("Search 1:", "Passed" if search(tree, 1) else "Failed")

    except Exception:
        print("Implementation Error: Please check your implementation of sorted, insert and search.")

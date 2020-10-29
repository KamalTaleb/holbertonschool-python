#!/usr/bin/python3
"""
    nqueens.py
"""
import sys


def n_queen(temp_store, store, column, i, n):
    
    if (i > n):
        store.append(temp_store[:])
        return store

    for j in range(n + 1):
        if i == 0 or ([i - 1, j - 1] not in temp_store and
                      [i - 1, j + 1] not in temp_store and
                      j not in col):
            if i > 1:
                t = 0
                for k in range(2, i + 1):
                    if ([i - k, j - k] in temp_store) or ([i - k, j + k] in temp_store):
                        t = 1
                        break
                if dia:
                    continue
            temp_store.append([i, j])
            column.append(j)
            n_queen(temp_store, store, column, i + 1, n)
            column.pop()
            temp_store.pop()

    return store

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    n_queen_store = n_queen([], [], [], 0, n - 1)
    for i in n_queen_store:
        print(i)

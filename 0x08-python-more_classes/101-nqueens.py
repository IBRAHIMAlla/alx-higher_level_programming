#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an N×N chessboard so that no two queens attack each other
"""


from sys import argv

if __name__ == "__main__":
    o = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize
    for m in range(n):
        o.append([m, None])

    def already_exists(y):
        """already_exists"""
        for w in range(n):
            if y == o[w][1]:
                return True
        return False

    def reject(x, y):
        """reject"""
        if (already_exists(y)):
            return False
        m = 0
        while(m < x):
            if abs(o[m][1] - y) == abs(m - x):
                return False
            m += 1
        return True

    def clear_a(x):
        """clear_a"""
        for m in range(x, n):
            o[m][1] = None

    def nqueens(x):
        """nqueens"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                o[x][1] = y
                if (x == n - 1):  # Receives the solution
                    print(o)
                else:
                    nqueens(x + 1)  # moves on to next x value

    # start at x = 0
    nqueens(0)

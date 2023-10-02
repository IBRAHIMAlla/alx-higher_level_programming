#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an N×N chessboard so that no two queens attack each other
"""


from sys import argv

if __name__ == "__main__":
    a = []
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
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """already_exists"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """reject"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clear_a"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """nqueens"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):  # Receives the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value

    # start x = 0
    nqueens(0)

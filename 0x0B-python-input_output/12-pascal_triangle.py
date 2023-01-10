#!/usr/bin/python3
"""Define a function Pascal Triangle."""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        pscl_t = triangles[-1]
        oth = [1]
        for i in range(len(pscl_t) - 1):
            oth.append(pscl_t[i] + pscl_t[i + 1])
        oth.append(1)
        triangles.append(oth)
    return triangles

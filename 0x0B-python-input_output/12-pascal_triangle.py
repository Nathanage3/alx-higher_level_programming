#!/usr/bin/python3
"""Generate Pascal's Triangle up to n rows."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        last_row = triangle[-1]
        # Generating the middle values of the row
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle

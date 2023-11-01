import numpy as np

# This script contains the methods and code of exercise 3. The script creates a nxn matrix filled with random values and
# returns a 1D array of the elements sorted in the "serpentine" order of the JPEG algorithm.


def zig_zag_index(k, n):
    # upper side of interval
    if k >= n * (n + 1) // 2:
        i, j = zig_zag_index(n * n - 1 - k, n)
        return n - 1 - i, n - 1 - j
    # lower side of interval
    i = int((np.sqrt(1 + 8 * k) - 1) / 2)
    j = k - i * (i + 1) // 2
    return (j, i - j) if i & 1 else (i - j, j)


def serpentine(n):  # creates a random matrix and returns a 1-D array with the components from the serpentine scan
    array_1D = []
    M = np.random.randint(255, size=(n, n))  # create a nxn matrix with random values [0-255] that represents an image
    print(M)
    for k in range(n * n):
        array_1D.append(M[zig_zag_index(k, n)])
    return array_1D


print(serpentine(n = 8))

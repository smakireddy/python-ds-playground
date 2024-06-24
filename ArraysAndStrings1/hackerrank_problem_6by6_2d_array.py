"""
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    biggest_glass = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1):
            print("arr {} {} => {}".format(i, j, arr[i][j]))
            hSum = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][
                j] + arr[i + 1][j + 1]
            if hSum > biggest_glass:
                biggest_glass = hSum

            print(hSum)
    return biggest_glass


if __name__ == '__main__':
    # arr = [[-9, -9, -9, 1, 1, 1],
    #        [0, -9, 0, 4, 3, 2],
    #        [-9, -9, -9, 1, 2, 3],
    #        [0, 0, 8, 6, 6, 0],
    #        [0, 0, 0, -2, 0, 0],
    #        [0, 0, 1, 2, 4, 0]
    #        ]
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    arr = [[-1, -1, 0 ,-9, -2, -2],
           [-2, -1, -6, -8, -2, -5],
           [-1, -1, -1, -2, -3, -4],
           [-1, -9, -2, -4, -4, -5],
           [-7, -3, -3, -2, -9, -9],
           [-1, -3, -1, -2, -4, -5]]
    result = hourglassSum(arr)
    print(result)

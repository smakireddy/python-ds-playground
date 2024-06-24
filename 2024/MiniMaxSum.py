#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Example
# [1,3,5,7,9]
# 1+3+5+7 = 16
# 3+5++7+9 = 24
# The minimum sum is  and the maximum sum is . The function prints
# 16 24

def miniMaxSum(arr):
    # Write your code here
    max_sum = sum(arr[1:])
    min_sum = sum(arr[:-1])
    print("{} {}".format(min_sum, max_sum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

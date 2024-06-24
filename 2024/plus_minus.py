#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    pos_ratio = len([n for n in arr if n > 0]) / l
    neg_ratio = len([n for n in arr if n < 0]) / l
    zero_ratio = 0 if (len([n for n in arr if n == 0]) == 0) else len([n for n in arr if n == 0]) / l

    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

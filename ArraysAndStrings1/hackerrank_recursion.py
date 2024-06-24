#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (n * factorial(n-1))



if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)

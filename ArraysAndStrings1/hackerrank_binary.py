"""
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

Example

The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    result = ""
    cnt, max = 0, 0
    while n > 0:
        remainder = 0 if n % 2 == 0 else 1
        flag = True
        n = math.floor(n / 2)
        print("remainder ->", remainder)
        result = str(remainder) + result
        if remainder == 1 and flag:
            cnt += 1
            flag = True
        else:
            flag = False
            if n != 0:
                cnt = 0
        if max < cnt:
            max = cnt

    print("Binary -> ", result)
    print("Count of consecutive 1's -> ", max)

"""
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

Example


The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Sample Input

Sample Input

aba
10

Sample Output
7

"""
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = 0
    length = len(s)
    if length == 1 and s[0] == 'a':
        return n

    print("cnt => ", int(cnt))

    if length >= n:
        for i in s[:n]:
            if i == 'a':
                cnt += 1
        return cnt
    else:
        m = math.floor(n / length)
        print("m => {}".format(m))

        c = n % length

        for i in range(length):
            if s[i] == 'a':
                cnt += 1

        cnt = (cnt * m)


        for i in s[:int(c)]:
            if i == 'a':
                cnt += 1

    return cnt


if __name__ == '__main__':
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    print(result)

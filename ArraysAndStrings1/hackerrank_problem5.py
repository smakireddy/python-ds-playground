"""There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes . Return .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: an array of binary integers
Returns

int: the minimum number of jumps required
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input

7
0 0 1 0 0 1 0

Sample Output

4

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = 0
    i = 0
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2] != 1:
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1

    return cnt


if __name__ == '__main__':
    n = 7
    c = [0, 0, 1, 0, 0, 1, 0]

    # expected output : 4
    result = jumpingOnClouds(c)
    print(result)

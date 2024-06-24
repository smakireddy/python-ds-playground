from collections import deque

from typing import List

"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""


class Solution:
    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n - 1 and j == n - 1:
                return d
            for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d + 1))
        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Q = deque()
        Q.append((0, 0, 1))
        R_len, C_len = len(grid), len(grid[0])
        print(f'R_len,C_len -> {R_len},{C_len}')
        while len(Q) > 0:
            r, c, level = Q.popleft()
            print(f'r , c , level -> {r},{c},{level}')
            if (r, c) == (R_len - 1, C_len - 1):
                return level
            for (nr, nc) in ((r - 1, c-1), (r - 1, c), (r -1 , c - 1),
                             (r, c - 1),(r,c+1),
                             (r+1,c-1),(r+1,c),(r+1,c+1)):
                print(f'before if nr,nc => {nr},{nc}')
                if (0 <= nr < R_len and 0 <= nc < C_len) and (grid[nr][nc] == 0):
                    print(f'nr,nc => {nr},{nc}')
                    Q.append((nr, nc, level + 1))
        return -1


if __name__ == '__main__':
    obj = Solution()
    grid = [[0, 1], [1, 0]]
    print(obj.shortestPathBinaryMatrix(grid))

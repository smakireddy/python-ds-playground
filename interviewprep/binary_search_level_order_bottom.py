"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
         3
        /\
       9  20
          /\
         15 7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]


"""
from queue import Queue
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom_better(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            raise Exception("Root is None")
        q = deque()
        q.append(root)
        res = []

        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)

            if level:
                res.append(level)

        return res


    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            raise Exception("Root is None!!")

        Q = Queue()
        res = []
        level = 0
        Q.put(root)
        while not Q.empty():
            arr = []
            size = Q.qsize() #Q.qsize()
            level += 1
            print(level)
            while size > 0:
                curr = Q.get()
                arr.append(curr.val)
                if curr.left is not None:
                    Q.put(curr.left)
                if curr.right is not None:
                    Q.put(curr.right)
                size -= 1
            if len(arr) > 0:
                if level%2 == 0:
                    res.append(arr)
                else:
                    res.append(arr[::-1])

        return res


if __name__ == '__main__':
    # tNode1 = TreeNode(3)
    # tNode2 = TreeNode(9)
    # tNode3 = TreeNode(20)
    # tNode4 = TreeNode(15)
    # tNode5 = TreeNode(7)
    # tNode1.left = tNode2
    # tNode1.right = tNode3
    # tNode3.left = tNode4
    # tNode3.right = tNode5
    #
    # sol = Solution()
    # result = sol.level_order_bottom(tNode1)
    # print(result)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    sol = Solution()
    result = sol.level_order_bottom_better(root)
    # result = sol.level_order_bottom(root)
    print(result)
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

values of the nodes you can see ordered from top to bottom.

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        current_depth = -1
        ans = []
        dq = deque()
        dq.append((root, 0))

        while dq:
            node, depth = dq.popleft()
            if depth > current_depth:
                ans.append(node.val)
                current_depth = depth

            if node.right:
                dq.append((node.right, depth + 1))

            if node.left:
                dq.append((node.right, depth + 1))

        return ans


if __name__ == '__main__':
    root = TreeNode(1,None,None)
    root.right = TreeNode(1,None,None)

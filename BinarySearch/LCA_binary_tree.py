"""

Lowest Common Ancestor in a Binary Search Tree.
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree.

BST_LCA

Input: LCA of 10 and 14
Output:  12
Explanation: 12 is the closest node to both 10 and 14
which is a ancestor of both the nodes.

Input: LCA of 8 and 14
Output:  8
Explanation: 8 is the closest node to both 8 and 14
which is a ancestor of both the nodes.

Input: LCA of 10 and 22
Output:  20
Explanation: 20 is the closest node to both 10 and 22
which is a ancestor of both the nodes.


                  20
                /    \
             8        22
            /\
          4   12
              /\
            10  14


"""

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1,n2):
    #Base Case
    if root is None:
        return None

    #if both n1 and n2 smaller than root , then lca lies left
    if (root.data>n1) and (root.data>n2) :
        return lca(root.left,n1,n2)

    #if both n1 and n2 greater than root. then lca lies right
    if (root.data<n1) and (root.data<n2):
        return lca(root.right,n1,n2)

    #you are left with LCA
    return root.data


root = node(20)
root.left = node(8)
root.right = node(22)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)


"""
Input: LCA of 10 and 14
Output:  12
Explanation: 12 is the closest node to both 10 and 14
which is a ancestor of both the nodes.
"""
n1 = 10 ; n2 = 14
result = lca(root, n1,n2)
print("LCA of {} and {} is {}".format(n1,n2,result))


"""
Input: LCA of 8 and 14
Output:  8
Explanation: 8 is the closest node to both 8 and 14
which is a ancestor of both the nodes.
"""
n1 = 8 ; n2 = 14
result = lca(root, n1,n2)
print("LCA of {} and {} is {}".format(n1,n2,result))















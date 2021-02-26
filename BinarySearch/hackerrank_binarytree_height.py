class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_height(self, root):

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)

        return 1 + max(lh, rh)

    def level_order(self, root):
        h = self.get_height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)

    def printLevelOrder(self, root):
        # Base case
        if root is None:
            return

        # Create an empty queue for level order traversal
        # Enqueue root and initialize height
        queue = [root]

        while len(queue) > 0:
            # print front of queue and remove it from queue
            print(queue[0].data, end=" ")
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def printLevelOrderZigZag(self,root):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            print(queue[0].data, end=" ")
            node = queue.pop(0)

            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    height = myTree.get_height(root)
    print(height)
    myTree.level_order(root)

    print("\n*********print from the printLevelOrder*******")
    myTree.printLevelOrder(root)
    print("\n*********print from the printLevelOrderZigZag*******")
    myTree.printLevelOrderZigZag(root)

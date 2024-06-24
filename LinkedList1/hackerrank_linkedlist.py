class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end='->')
            current = current.next

    def insert(self, head, data):

        if head is None:
            head = Node(data)
            return head
        itr = head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
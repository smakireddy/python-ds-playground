"""
Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class swapNodes:
    def __init__(self):
        self.head = Node(data, None)

    def swapPairs(self, head: Node) -> Node:
        if not head or not head.next:
            return head

        def swap(head, last):
            if head.next is not None:
                head.val, last.val = last.val, head.val

                if head.next.next is not None:
                    return swap(head.next.next, last.next.next)
                else:
                    return
            else:
                return

        swap(head, head.next)

        return head

    def in_place_value(self, head):
        if not head: return head
        first = head
        second = head.next
        while first and second:
            first.val, second.val = second.val, first.val
            first = second.next
            if not first: break
            second = second.next.next
        return head

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    obj = swapNodes()
    obj.insert_values([1, 2, 3, 4])
    print(obj)

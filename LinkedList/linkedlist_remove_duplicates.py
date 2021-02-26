class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next


if __name__ == '__main__':
    ll = LinkedList()
    first_node = Node(1)
    ll.head = first_node
    second_node = Node(2)
    ll.head.next = second_node
    third_node = Node(3)
    ll.head.next.next = third_node
    fourth_node = Node(3)
    ll.head.next.next.next = fourth_node
    fivth_node = Node(4)
    ll.head.next.next.next.next = fivth_node
    print(ll)
    print("****************")
    ll.removeDuplicates()
    print(ll)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_end_som(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data_to_insert)
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data_to_remove):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_to_remove:
                self.remove_at(count)
                break

            itr = itr.next
            count += 1

    def reverseList(self, head):
        prev = None
        curr = self.head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(20)
    # ll.insert_at_begining(10)
    # ll.print()
    # ll.insert_at_end(30)
    # ll.insert_at_end(40)
    # ll.print()
    ll.insert_at_begining(10)
    ll.insert_at_end(20)
    ll.insert_at(1, 15)
    ll.print()

    ll.insert_after_value(10, 12)
    ll.print()

    ll.remove_by_value(35)
    ll.print()
    ll.reverseList(10)
    ll.print()
    print("length of linked list is : ", ll.get_length())
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.insert_at(1,"blueberry")
    # ll.remove_at(2)
    # ll.print()
    #
    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()

class Node:
    def __init__(self, val=None, next_=None, prev=None):
        self.val = val
        self.next_ = next_
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):
        node_node = Node(val)
        if self.head:
            self.head.prev = node_node
            node_node.next_ = self.head
        self.head = node_node

    def insertAfter(self, val):
        new_node = Node(val)
        node = self.head



    def delete(self, val):
        pass

    def search(self, val):
        pass

    def print_(self):
        node = self.head

        while node:
            print(node.val)
            node = node.next_


dll = DoubleLinkedList()
dll.insert(10)
dll.insert(20)

dll.print_()



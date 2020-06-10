class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node



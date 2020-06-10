class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return -1

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]
        return -1

    def get_stack(self):
        return self.items

    def is_empty(self):
        return len(self.items) == 0




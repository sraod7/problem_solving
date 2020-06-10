class Node:
    left = None
    right = None
    val = None

    def __init__(self, value):
        self.val = value

    def insert(self, value):
        if value <= self.val:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.val == value:
            return True
        if value < self.val:
            if not self.left:
                return False
            self.left.contains(value)
        else:
            if not self.right:
                return False
            self.right.contains(value)

root = Node(5)
root.insert(8)
root.insert(4)
root.insert(2)
root.insert(6)

print(root.contains(2))
print(root.contains(67))



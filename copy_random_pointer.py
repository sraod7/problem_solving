class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Node) -> Node:
    map_ = {}

    while head:
        map_[head] = Node(head.val)
        head = head.next

    res = Node(-1)
    copy = res

    for original_node, new_node in map_.items():
        copy.next = new_node
        if original_node.random:
            copy.next.random = map_[original_node.random]

        copy = copy.next

    return res.next
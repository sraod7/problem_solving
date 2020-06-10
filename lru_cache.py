class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map_ = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map_:
            self._update_node(key, self.map_[key].val)
            return self.map_[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map_:
            self._update_node(key, value)
        else:
            self._check_capacity()
            self._append_node(key, value)

    def print_(self):
        node = self.head
        a = []
        while node:
            a.append(node.val)
            node = node.next
        print(a)

    def _create_node(self, key, value):
        new_node = Node(value, key)
        nex = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        new_node.next = nex
        nex.prev = new_node
        self.map_[key] = new_node

    def _append_node(self, key, value):
        new_node = Node(value, key)
        prev = self.tail.prev
        new_node.prev = prev
        prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node

        self.map_[key] = new_node

    def _update_node(self, key, value):
        self._delete_node(key)
        self._append_node(key, value)

    def _delete_node(self, key):
        node = self.map_[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _check_capacity(self):
        if len(self.map_) == self.capacity:
            tail = self.tail.prev
            node = tail.prev
            node.prev.next = self.tail
            self.tail.prev = node.prev
            del self.map_[node.key]


# Your LRUCache object will be instantiated and called as such:
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj = LRUCache(2)
for val in [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]:
    if len(val) == 1:
        print(f'get {val}', obj.get(val[0]))
    else:
        print(f'put {val}', obj.put(val[0], val[1]))

    obj.print_()

# [null,null,1,null,-1,null,-1,3,4]

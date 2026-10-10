class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node()
        self.mru = Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        node.prev, node.next = prev, nxt
        prev.next = self.mru.prev = node

    def put(self, key: int, value: int) -> None:
        node = Node(key=key, val=value)
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self._remove(lru)
            del self.cache[lru.key]
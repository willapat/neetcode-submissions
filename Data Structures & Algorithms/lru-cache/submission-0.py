class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {} # map key to node

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):    
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])

        if len(self.mp) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]

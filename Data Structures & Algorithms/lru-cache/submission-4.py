class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        prevv = node.prev
        nexxt = node.next

        prevv.next = nexxt
        nexxt.prev = prevv
    
    def insert(self, node):
        prevv = self.right.prev

        prevv.next = node
        node.next = self.right

        self.right.prev = node
        node.prev = prevv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # delete Node
        self.delete(self.cache[key])

        # insert Node (right)
        self.insert(self.cache[key])

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            # delete Node
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next

            # delete LRU
            self.delete(lru)
            del self.cache[lru.key]

        

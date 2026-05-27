class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key:Node(key, val)
        self.capacity = capacity

        self.LEFT = Node()
        self.RIGHT = Node()

        self.LEFT.next = self.RIGHT
        self.RIGHT.prev = self.LEFT
    
    def delete(self, node):
        prevv = node.prev
        nexxt = node.next

        prevv.next = node.next
        nexxt.prev = node.prev
    
    def insert(self, node):
        prevv = self.RIGHT.prev

        prevv.next = node
        node.next = self.RIGHT

        node.prev = prevv
        self.RIGHT.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # delete Node(key)
        self.delete(self.cache[key])

        # insert Node(key) to RIGHT
        self.insert(self.cache[key])

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #delete Node(key)
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        # insert Node(key) to RIGHT
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.LEFT.next

            #delete lru node
            self.delete(lru)

            del self.cache[lru.key]
        

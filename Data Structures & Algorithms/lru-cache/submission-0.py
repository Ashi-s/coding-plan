class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key is same, value pointing to node 
        
        # create two Nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # point both nodes to each other
        # left node (next pointer) points to --> LRU (Least Recent Used)
        # right node (prev pointer) points to --> Most Recent Used
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        prevv = node.prev
        nextt = node.next

        prevv.next = nextt
        nextt.prev = prevv
    
    def insert(self, node):
        # always insert before right
        prevv = self.right.prev
        nextt = self.right

        prevv.next = node
        node.next = nextt

        nextt.prev = node
        node.prev = prevv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # delete the node and put in before right pointer
        self.delete(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove lru (node next to left)
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        

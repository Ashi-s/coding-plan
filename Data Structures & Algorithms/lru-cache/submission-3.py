class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        prevv = node.prev
        nextt = node.next

        prevv.next = nextt
        nextt.prev = prevv
    
    def insert(self, node):
        prevv = self.right.prev

        prevv.next = node
        node.next = self.right

        self.right.prev = node
        node.prev = prevv
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        #delete node(key)
        self.delete(self.cache[key])

        #insert node(key) to end(right)
        self.insert(self.cache[key])

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        
        #insert node(key) to end(right)
        self.insert(self.cache[key])
        

        # if capacity increases
        if len(self.cache) > self.capacity:
            lru = self.left.next

            #delete node(lru)
            self.delete(lru)

            #remove lru from cache
            del self.cache[lru.key]



                

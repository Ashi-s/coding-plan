class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = Node(homepage)
        self.curr = self.browser

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next = node
        node.prev = self.curr

        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:

        while steps > 0:
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
            steps -= 1
        
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
            steps -= 1
        
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
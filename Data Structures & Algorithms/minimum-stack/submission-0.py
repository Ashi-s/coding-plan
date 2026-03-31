class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
        

    def pop(self) -> None:
        if len(self.st) > 0:
            self.st.pop()
        
        if len(self.minStack) > 0:
            self.minStack.pop()

        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        

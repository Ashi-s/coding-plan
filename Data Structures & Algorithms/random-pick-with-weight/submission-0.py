class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(self.w)
        

    def pickIndex(self) -> int:
        target = self.total * random.random() # between 0.0 & 1.0

        curr = 0
        for i in range(len(self.w)):
            curr += self.w[i]

            if curr > target:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
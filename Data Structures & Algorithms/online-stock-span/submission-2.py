class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        count = 1

        for i in range(len(self.st)-1, -1, -1):
            if self.st[i] <= price:
                count += 1
            else:
                self.st.append(price)
                return count
        self.st.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
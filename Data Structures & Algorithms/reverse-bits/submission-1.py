class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1               # get the ith bit
            res = res | (bit << (31-i))      # insert i th (31-i)
        return res

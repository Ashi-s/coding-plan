class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num = i
            count = 0
            while num:
                if num % 2 != 0:
                    count += 1
                num = num >> 1
            
            res.append(count)
        return res
                 
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        count = 0
        res = float('inf')
        for r in range(len(blocks)):
            if (r - l + 1) > k:
                if blocks[l] == 'W':
                    count -= 1
                l += 1

            if blocks[r] == 'W':
                count += 1
            
            if (r - l + 1) == k:
                res = min(res, count)
        
        return res
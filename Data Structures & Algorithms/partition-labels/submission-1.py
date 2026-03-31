class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = { char: i for i, char in enumerate(s) }

        end = 0
        res = []
        size = 0

        for i, char in enumerate(s):
            size += 1
            
            end = max(end, last_index[char])

            if i == end:
                res.append(size)
                size = 0
        
        return res
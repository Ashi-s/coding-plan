class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        # print(sorted(d, key = lambda x: d.get(x))[::-1])
        return sorted(d, key = lambda x: d.get(x))[::-1][:k]
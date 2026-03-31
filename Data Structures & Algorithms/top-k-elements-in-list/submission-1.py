class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        bucket = [[] for i in range(len(nums)+1)]
        
        for key, val in count.items():
            bucket[val].append(key)

        res = []
        for b in range(len(bucket)-1, 0, -1):
            for n in bucket[b]:
                res.append(n)
                if len(res) == k:
                    return res

    


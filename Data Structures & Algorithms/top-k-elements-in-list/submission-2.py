class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, val in count.items():
            bucket[val].append(key)
        
        print(bucket)
        for b in range(len(bucket)-1, 0, -1):
            for i in bucket[b]:
                res.append(i)
                print(res, k)
                if len(res) == k:
                    return res

                

        
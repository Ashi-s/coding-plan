class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(curr, res, visited, index_visit):
            # print(curr)
            if len(curr) == len(nums):
                if tuple(curr) not in visited:
                    res.append(curr.copy())
                    visited.add(tuple(curr))
                    return
            

            for i in range(len(nums)):
                if i not in index_visit:
                    index_visit.append(i)
                    curr.append(nums[i])
                    helper(curr, res, visited, index_visit)
                    curr.pop() 
                    index_visit.pop()       

        res = []
        visited = set()
        helper([], res, visited, [])
        
        return res
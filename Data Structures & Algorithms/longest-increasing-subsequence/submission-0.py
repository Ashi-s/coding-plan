class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(idx, curr, output):
            print(f"idx-{idx},curr-{curr},output-{output}")
            output[0] = max(output[0], len(curr))

            for j in range(idx+1, N):
                if nums[j] > nums[idx]:
                    curr.append(nums[j])
                    dfs(j, curr, output)

                    curr.pop()

        
        N = len(nums)
        res = 0
        for i in range(N):
            curr = [nums[i]]
            output = [1]
            dfs(i, curr, output)
            res = max(res, output[0])

        return res
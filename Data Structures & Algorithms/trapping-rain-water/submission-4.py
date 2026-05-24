class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix = [0] * N
        sufix = [0] * N
        
        prefix[0] = height[0]
        sufix[N-1] = height[N-1]

        res = 0

        for i in range(1, N):
            prefix[i] = max(prefix[i-1], height[i])
        
        for j in range(N-2, -1, -1):
            sufix[j] = max(sufix[j+1], height[j])
        
        for i in range(1, N):
            b = min(prefix[i], sufix[i]) 
            res +=  (b - height[i])
        
        return res
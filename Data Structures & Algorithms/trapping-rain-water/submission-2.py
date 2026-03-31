class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        print(f"left={left}")
        
        right[n-1] = height[n-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        print(f"right={right}")
        
        output = 0
        for i in range(len(height)):
            min_distance = min(left[i], right[i])
            if min_distance - height[i] > 0:
                output += (min_distance - height[i])
            print(f"output={output}")
        
        return output
        

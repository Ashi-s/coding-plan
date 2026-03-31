class Solution:
    def trap(self, height: List[int]) -> int:
        left = [ 0 for i in range(len(height))]
        right = [0 for i in range(len(height))]

        max_left = height[0]
        max_right = height[-1]

        for i in range(1, len(height)):
            left[i] = max(max_left, left[i-1])
            max_left = max(max_left, height[i])
        print(f"left={left}")
        
        for i in range(len(height)-2, -1, -1):
            right[i] = max(max_right, height[i+1])
            max_right = max(max_right, height[i])
        print(f"right={right}")
        
        output = 0
        for i in range(len(height)):
            min_distance = min(left[i], right[i])
            if min_distance - height[i] > 0:
                output += (min_distance - height[i])
            print(f"output={output}")
        
        return output
        

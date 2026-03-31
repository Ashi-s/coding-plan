class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #(index, height)
        maxArea = 0

        for i in range(len(heights)):
            start = i

            while st and st[-1][1] > heights[i]:
                index, height = st.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            st.append((start, heights[i]))
        
        while st:
            idx, h = st.pop()
            maxArea = max(maxArea, (len(heights) - idx) * h)
        return maxArea
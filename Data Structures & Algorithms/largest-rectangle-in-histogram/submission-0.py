class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                maxArea = max(maxArea, (i-index) * height)
                start = index
            st.append((start, h))
        
        while st:
            i, h = st.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea

        
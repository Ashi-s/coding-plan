class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = [] #(index, height)

        for i in range(len(heights)):
            start = i

            while st and st[-1][1] > heights[i]:
                index, height = st.pop()
                maxArea = max(maxArea, (i-index)* height)
                start = index
            
            st.append((start, heights[i]))
        
        while st:
            idx, hei = st.pop()
            maxArea = max(maxArea, (len(heights)-idx)* hei)
        
        return maxArea
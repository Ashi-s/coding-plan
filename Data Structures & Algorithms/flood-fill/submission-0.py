class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def helper(r, c, val):
            dir = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]

            for row, col in dir:
                if 0 <= row < M and 0 <= col < N and (row, col) not in visited and image[row][col] == val:
                    image[row][col] = color
                    visited.add((row, col))
                    helper(row, col, val)

        


        M, N = len(image), len(image[0])
        visited = set()

        if image[sr][sc] == color:
            return image

        visited.add((sr, sc))
        helper(sr, sc, image[sr][sc])
        image[sr][sc] = color
        return image
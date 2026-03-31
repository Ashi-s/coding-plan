class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # go right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            # go down
            for j in range(top, bottom+1):
                res.append(matrix[j][right])
            right -= 1

            # go left
            if top <= bottom:
                for k in range(right, left-1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1

            # go up
            if left <= right:
                for l in range(bottom, top-1, -1):
                    res.append(matrix[l][left])
                left += 1

        return res
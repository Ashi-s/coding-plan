class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                print(l, r, mid)

                if target == arr[mid]:
                    return True
                elif target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return False 
        
        for row in matrix:
            if target == row[0] or target == row[-1]:
                return True
            elif row[0] < target < row[-1]:
                print("calling binary search")
                print(row)
                return binary_search(row)
        return False
                
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, R, M):
            left, right = arr[L:M+1], arr[M+1:R+1]
            idx, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[idx] = left[j]
                    j += 1
                else:
                    arr[idx] = right[k]
                    k += 1
                idx += 1
            
            while j < len(left):
                arr[idx] = left[j]
                j += 1
                idx += 1
            
            while k < len(right):
                arr[idx] = right[k]
                k += 1
                idx += 1


        def mergeSort(arr, l, r):
            if l >= r:
                return

            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)

            merge(arr, l, r, mid)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums

        
        
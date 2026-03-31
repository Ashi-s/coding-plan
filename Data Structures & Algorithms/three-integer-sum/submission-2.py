class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(arr, n):
            l, r = 0, len(arr) - 1

            while l < r:
                if (n + arr[l] + arr[r]) > 0:
                    r -= 1
                elif (n + arr[l] + arr[r]) < 0:
                    l += 1
                else:
                    res.append([n, arr[l], arr[r]])
                    l += 1
                    r -= 1
                    # FIX 1: Skip duplicates for the second number
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
                    # FIX 2: Skip duplicates for the third number
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1

             
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1, 2]      
        nums.sort()
        res = []
        i = 0

        while (i < len(nums)-2):
            # while nums[i] == nums[i+1] and i < len(nums)-2:
            #     i += 1
            
            twoSum(nums[i+1:], nums[i])
            while nums[i] == nums[i+1] and i < len(nums)-2:
                i += 1
            i += 1
        return res

        
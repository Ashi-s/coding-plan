class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Idx = { n: i for i, n in enumerate(nums2) }

        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            idx = nums2Idx[nums1[i]]

            for j in range(idx+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        
        return res
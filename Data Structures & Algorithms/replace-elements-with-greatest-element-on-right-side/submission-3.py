class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        _max = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = _max
            _max = max(_max, tmp)
        
        arr[-1] = -1
        return arr

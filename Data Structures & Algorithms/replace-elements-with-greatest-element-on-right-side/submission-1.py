class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # for i in range(len(arr)):
        #     _max = 0
        #     for j in range(i+1, len(arr)):
        #         _max = max(_max, arr[j])
            
        #     arr[i] = _max
        
        # arr[-1] = -1

        # return arr

        _max = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = _max
            _max = max(_max, tmp)
        
        arr[-1] = -1
        return arr

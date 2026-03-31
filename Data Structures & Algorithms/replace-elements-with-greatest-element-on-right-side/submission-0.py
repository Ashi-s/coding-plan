class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            _max = 0
            for j in range(i+1, len(arr)):
                _max = max(_max, arr[j])
            
            arr[i] = _max
        
        arr[-1] = -1

        return arr
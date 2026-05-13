class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            output = []
            for j in range(len(res[-1])+1): #next row = prev + 1
                output.append(temp[j] + temp[j+1])
            
            res.append(output)
        
        return res[-1]
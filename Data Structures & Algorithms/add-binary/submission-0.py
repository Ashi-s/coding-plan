class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            # 1. Get current digits or 0 if out of bounds
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0
            
            # 2. Calculate the total sum for this position
            total = val_a + val_b + carry
            
            # 3. Update digit and carry
            # total % 2 gives the binary digit (0 or 1)
            # total // 2 gives the carry (1 if total >= 2, else 0)
            res.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
        
        # 4. Reverse the list and join to form the final string
        return ''.join(res[::-1])

            
            

            


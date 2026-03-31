class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        add = True

        for i in range(len(digits)-1, -1, -1):
            if add:
                summ = digits[i] + 1
                add = False
            else:
                summ = digits[i] + carry

            if summ > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = summ
                carry = 0
        
        if carry:
            digits.insert(0, carry)
        
        return digits
                
                
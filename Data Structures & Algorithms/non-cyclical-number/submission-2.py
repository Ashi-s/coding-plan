class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n == 1:
            return True

        while n != 1:

            if n in seen:
                return False
            seen.add(n)
            
            summ = 0

            while n != 0:
                mod = n % 10
                summ += (mod * mod)
                n = n // 10
            print(summ)
            if summ == 1:
                return True

            n = summ
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {}

        for b in bills:
            get_5 = d.get(5, 0)
            get_10 = d.get(10, 0)
            if b == 5:
                d[5] = 1 + get_5
            elif b == 10:
                if get_5 > 0:
                    d[5] -= 1
                    d[10] = 1 + get_10
                else:
                    return False
            else:
                if get_10 >= 1 and get_5 >= 1:
                    d[10] -= 1
                    d[5] -= 1
                elif get_5 >= 3:
                    d[5] -= 3
                else:
                    return False
        
        return True
            
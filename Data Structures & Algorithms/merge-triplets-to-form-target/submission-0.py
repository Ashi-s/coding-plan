class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        aj, bj, cj = target
        curr = [0,0,0]

        for t in triplets:
            ai, bi, ci = t

            # if any of them is greater than target
            if ai > aj or bi > bj or ci > cj:
                continue
            else:
                curr = [max(ai, curr[0]), max(bi, curr[1]), max(ci, curr[2])]
        
        return curr == target
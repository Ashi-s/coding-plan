class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}

        for h in hand:
            d[h] = d.get(h, 0) + 1
        
        hand.sort()
        
        # for h in hand:
        #     if d[h] <= 0:
        #         continue
        #     # start card
        #     elif (h-1 not in d or d[h-1] <= 0) and h in d and d[h] > 0:
        #         curr_hand = h
        #         for i in range(groupSize):
        #             if curr_hand in d and d[curr_hand] > 0:
        #                 d[curr_hand] -= 1
        #             else:
        #                 return False
                    
        #             curr_hand += 1
        #     elif h-1 in d and d[h-1] > 0:
        #         continue
        
        # return True

        if len(hand) % groupSize != 0:
            return False

        for h in hand:
            if d[h] > 0:
                for i in range(h, h + groupSize):
                    if d.get(i, 0) > 0:
                        d[i] -= 1
                    else:
                        return False
        
        return True

        

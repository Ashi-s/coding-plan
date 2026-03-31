class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Recursion - TLE
        # def helper(curr, count):
        #     if curr == amount:
        #         self.output = min(self.output, count)
        #         return
            
        #     if curr > amount:
        #         return
            
        #     for c in coins:
        #         helper(curr+c, count+1)

        
        # self.output = float('inf')
        # helper(0, 0)
        # return self.output if self.output != float('inf') else -1


        # DP
        memo = {}
        def helper(amount):
            if amount in memo:
                return memo[amount]
            
            if amount == 0:
                return 0
            
            if amount > amount:
                return 0
            
            res = float('inf')
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + helper(amount - c))
            memo[amount] = res
            return res
        
        minCoins = helper(amount)
        return helper(amount) if minCoins != float('inf') else -1
            

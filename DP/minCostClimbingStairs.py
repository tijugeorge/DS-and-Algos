class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. A function that returns the answer
        def dp(i):
            if i <= 1:
                # 3. Base cases
                return 0
            
            if i in memo:
                return memo[i]
            
            # 2. Recurrence relation
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))

    #above is top down approach ith time complexity chnaged from O(2^n) to O(n)

    #below is bottom-up implementation - the base cases and recurrence relation are the same, we just need to use an array instead of a function.    
        def minCostClimbingStairs(self, cost: List[int]) -> int:
            n = len(cost)
            # 1. An array that stores the answers
            dp = [0] * (n + 1)
            
            # 3. Base cases are implicitly defined as they are 0
    
            for i in range(2, n + 1):
                # 2. Recurrence relation
                dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
            return dp[n]  

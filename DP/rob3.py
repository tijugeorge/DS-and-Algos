    def rob3(self, nums): #bottom-up approach
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        dp = [0]*n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[n-1]

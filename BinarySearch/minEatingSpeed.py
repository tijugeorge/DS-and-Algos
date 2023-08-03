class Solution:
    def minEatingSpeed(self, piles, h):
        def check(k):
            hours = 0
            for bananas in piles:
                hours+=ceil(bananas/k)
            return hours<=h
        
        left = 1
        right = max(piles)
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left
    
piles = [3,6,7,11]
h = 2
SS= Solution()
print(SS.minEatingSpeed(piles, h))

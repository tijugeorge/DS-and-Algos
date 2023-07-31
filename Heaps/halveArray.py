class Solution:
    def halveArray(self, nums):
        target = sum(nums)/2
        heap = [-num for num in nums]  # negative as it is a max heap
        heapq.heapify(heap)
        
        ans = 0 # count the opertions
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x/2 #reducing to half and since all numbers are negative we add by half
            heapq.heappush(heap, x/2)
        return ans
    
array = [5,19,8,1]
ss=Solution()
print(ss.halveArray(array))

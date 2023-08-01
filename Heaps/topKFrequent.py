from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        heap = []
        
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) >k:
                heapq.heappop(heap)
         
        return [pair[1] for pair in heap]
        

SS= Solution()
k= 2
nums = [1,3,2,2,1,2,3,2,1,1,1,3]
print(SS.topKFrequent(nums,k))

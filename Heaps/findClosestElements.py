import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        heap = []
        
        for num in arr:
            distance = abs(x-num)
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-pair[1] for pair in heap])

        

SS= Solution()
k= 2
x=3
nums = [1,3,2,2,1,2,3,2,1,1,1,3]
print(SS.findClosestElements(nums,k, x))

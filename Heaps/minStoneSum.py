class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for i in range(k):
            curr = -heapq.heappop(heap) # negataive as to be in consistence with the max heap array i.e piles
            remove = curr//2
            heapq.heappush(heap, -(curr - remove)) #again negaive to be in consistence

        return -sum(heap)  # negative to remove the negative sign

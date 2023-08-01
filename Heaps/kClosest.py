import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            val = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (val, point))
        res = []
        while len(res) < k:
            (val, point) = heapq.heappop(heap)
            res.append(point)

        return res

import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            
            if first != second:
                heapq.heappush(stones, -abs(first - second))
                
        return -stones[0] if stones else 0
    
    
stones = [2,7,4,1,8,1]

ss= Solution()
print(ss.lastStoneWeight(stones))

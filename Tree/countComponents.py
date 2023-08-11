class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        ans = 0
        
        for index in range(n):
            if index not in seen:
                self.dfshelper(index, edges, seen, graph)
                ans+=1
        return ans
        
        
    def dfshelper(self, index, edges, seen, graph):
        if index in seen:
            return
        seen.add(index)
        for neighbor in graph[index]:
            self.dfshelper(neighbor, edges, seen, graph)

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        # Mark the nodes in 'restricted' as visited.
        seen = [False]*n
        for node in restricted:
            seen[node] = True
            
        # Store all the nodes to be visited in 'queue'
        ans = 0
        queue = collections.deque([0])
        seen[0] = True
        
        while queue:
            currnode = queue.popleft()
            ans+=1
         
        # For all the neighbors of the current node, if we haven't visit it before, add it to 'queue' and mark it as visited.
            for nextnode in graph[currnode]:
                if not seen[nextnode]:
                    seen[nextnode] = True
                    queue.append(nextnode)
        return ans
        

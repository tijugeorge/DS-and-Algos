class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)    
        seen = [False]*n
        seen[source] = True
        stack =[source]
        
        while stack:
            curr_node = stack.pop()
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)
        return seen[destination]



#this is iterative

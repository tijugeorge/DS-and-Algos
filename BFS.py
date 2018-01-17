graph = {'A':['B', 'C', 'E'],
         'B':['A', 'D', 'E'],
         'C':['A', 'F', 'G'],
         'D':['B','E'],
         'E':['A','B','D'],
         'F':['C'],
         'G':['C']}


def bfs_connected_component(graph, start):
	explored = []
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbors = graph[node]

			for neighbor in neighbors:
				queue.append(neighbor)
	return explored

	

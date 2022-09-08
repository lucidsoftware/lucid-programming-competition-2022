from collections import defaultdict
from heapq import heappush, heappop
def cheapestCostToBuildBridges(grid):
	m, n = len(grid), len(grid[0])
	# label islands
	def label(i, j, v):
		if i < m and i >= 0 and j < n and j >= 0 and grid[i][j] == 1:
			grid[i][j] = v
			label(i+1, j, v)
			label(i, j+1, v)
			label(i-1, j, v)
			label(i, j-1, v)
	
	label_index = 2
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				label(i, j, label_index)
				label_index += 1
	
	# find all bridges and add them to a graph
	graph = defaultdict(lambda : defaultdict(lambda : float("inf")))
	for i in range(m):
		prev, dist = None, -1
		for j in range(n):
			if grid[i][j]:
				if prev and prev != grid[i][j]:
					graph[prev][grid[i][j]] = min(dist, graph[prev][grid[i][j]])
					graph[grid[i][j]][prev] = min(dist, graph[grid[i][j]][prev])
				prev = grid[i][j]
				dist = -1
			dist += 1
	for j in range(n):
		prev, dist = None, -1
		for i in range(m):
			if grid[i][j]:
				if prev != None and prev != grid[i][j]:
					graph[prev][grid[i][j]] = min(dist, graph[prev][grid[i][j]])
					graph[grid[i][j]][prev] = min(dist, graph[grid[i][j]][prev])
				prev = grid[i][j]
				dist = -1
			dist += 1
	
	# minimum spanning tree
	notVisited = set(i for i in range(2, label_index))
	priorityQueue = [(0, 2)]
	out = 0
	while priorityQueue:
		cost, index = heappop(priorityQueue)
		if index in notVisited:
			out += cost
			notVisited.remove(index)
			for adj in graph[index]:
				heappush(priorityQueue, (graph[index][adj], adj))
	return -1 if notVisited else out


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(cheapestCostToBuildBridges(grid))
	

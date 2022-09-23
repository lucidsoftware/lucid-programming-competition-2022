import heapq
from collections import defaultdict

BIG = 999999

M, N = [int(ea) for ea in input().split(' ')]
grid = []
for m in range(M):
    grid.append([int(ea) for ea in input().split(' ')])

# find islands with floodfill
islandCounter = 2
for m in range(M):
    for n in range(N):
        if grid[m][n] != 1:
            continue
        q = [(m, n)]
        while q:
            x, y = q.pop(0)
            if x < 0 or x >= M or y < 0 or y >= N:
                continue
            if grid[x][y] == 1:
                grid[x][y] = islandCounter
                q.append((x+1, y))
                q.append((x-1, y))
                q.append((x, y+1))
                q.append((x, y-1))
        islandCounter += 1

# find bridges by scanning vertically then horizontally, looking for lines of 0s between islands
# neighbors: island => [(island, cost)]
neighbors = defaultdict(list)
for m in range(M):
    prev = None
    counter = 0
    for n in range(N):
        if grid[m][n] != 0:
            if prev and prev != grid[m][n]:
                neighbors[prev].append((grid[m][n], counter))
                neighbors[grid[m][n]].append((prev, counter))
            prev = grid[m][n]
            counter = 0
        else:
            counter += 1

for n in range(N):
    prev = None
    counter = 0
    for m in range(M):
        if grid[m][n] != 0:
            if prev and prev != grid[m][n]:
                neighbors[prev].append((grid[m][n], counter))
                neighbors[grid[m][n]].append((prev, counter))
            prev = grid[m][n]
            counter = 0
        else:
            counter += 1

startNode = 2  # first island is always 2

# all islands start infinitely far away
shortestBridgeToIsland = {}
for i in range(2, islandCounter):
    shortestBridgeToIsland[i] = BIG

# add start island's bridges
nextClosest = []
for i, c in neighbors[startNode]:
    shortestBridgeToIsland[i] = min(shortestBridgeToIsland[i], c)
    heapq.heappush(nextClosest, (shortestBridgeToIsland[i], i))

unlinkedIslands = set(range(3, islandCounter))
totalCost = 0
while unlinkedIslands:
    shortestI = 2
    shortestC = BIG
    while shortestI not in unlinkedIslands:
        if len(nextClosest) == 0:
            shortestI = 2
            totalCost = BIG
            break
        shortestC, shortestI = heapq.heappop(nextClosest)
    if shortestI == 2:
        break
    for i, c in neighbors[shortestI]:
        shortestBridgeToIsland[i] = min(shortestBridgeToIsland[i], c)
        heapq.heappush(nextClosest, (shortestBridgeToIsland[i], i))
    totalCost += shortestC
    unlinkedIslands.remove(shortestI)

print(totalCost if totalCost < BIG else -1)

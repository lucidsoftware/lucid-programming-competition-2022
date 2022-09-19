N, M, X = [int(ea) for ea in input().split(' ')]

"""
Each grid location will be (score, fish)
For each move, will claim spot if score is lower
"""

BIG = 999999
LAND = 'land'
WATER = 'water'

def convertStartingLocation(startingChar: str):
    if startingChar == '-1':
        return -1, LAND
    if startingChar == '0':
        return BIG, WATER
    return 0, startingChar

grid = []
startingFish = {}
for n in range(N):
    line = input().replace('  ', ' ').split(' ')
    for i, f in enumerate(line):
        if f == '0' or f == '-1':
            continue
        if f not in startingFish:
            startingFish[f] = []
        startingFish[f].append((n, i))
    grid.append([convertStartingLocation(ea) for ea in line])

for f in sorted(startingFish.keys()):
    for x, y in startingFish[f]:
        # BFS
        visited = set()
        q = [(x,y,1)]
        while len(q) > 0:
            cx, cy, cs = q.pop(0)  # current x, current y, current score
            # consider adding each cardinal direction
            if cx > 0:
                ns, nf = grid[cx - 1][cy]  # next score, next fish
                if ns > cs:
                    grid[cx - 1][cy] = (cs, f)
                    q.append((cx - 1, cy, cs + 1))
            if cx < N-1:
                ns, nf = grid[cx + 1][cy]
                if ns > cs:
                    grid[cx + 1][cy] = (cs, f)
                    q.append((cx + 1, cy, cs + 1))
            if cy > 0:
                ns, nf = grid[cx][cy - 1]
                if ns > cs:
                    grid[cx][cy - 1] = (cs, f)
                    q.append((cx, cy - 1, cs + 1))
            if cy < N-1:
                ns, nf = grid[cx][cy + 1]
                if ns > cs:
                    grid[cx][cy + 1] = (cs, f)
                    q.append((cx, cy + 1, cs + 1))

fishCount = {}
for r in grid:
    for s, f in r:
        if f == WATER or f == LAND:
            continue
        if f not in fishCount:
            fishCount[f] = 0
        fishCount[f] += 1

print(max(fishCount, key=fishCount.get))

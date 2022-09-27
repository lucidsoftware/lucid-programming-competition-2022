import heapq
from collections import Counter

n, m, x = map(int, input().split())
g = [input().split() for _ in range(n)]

q = []
for i in range(n):
    for j in range(m):
        if g[i][j] not in ['0', '1']:
            heapq.heappush(q, (0, g[i][j], i, j)) # (step, type, r, c)
            g[i][j] = '0'

dirs = [1, 0, -1, 0, 1]
counts = Counter()
while q:
    step, fish, r, c = heapq.heappop(q)
    if r < 0 or r >= n or c < 0 or c >= m or g[r][c] != '0':
        continue

    g[r][c] = fish
    counts[fish] += 1
    for i in range(4):
        heapq.heappush(q, (step+1, fish, r+dirs[i], c+dirs[i+1]))

print(counts.most_common(1)[0][0])
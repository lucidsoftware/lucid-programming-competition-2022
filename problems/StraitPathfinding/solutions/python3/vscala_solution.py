from collections import deque
m, n = int(input()), int(input())
port = [[c for c in input()] for _ in range(m)]

start = None
boat_t = [{}] # time -> {(i, j) -> 0: down moving boat, 1: up moving boat}
obstacle = set()
for i, row in enumerate(port):
	for j, val in enumerate(row):
		if val == "~":
			continue
		elif val == "v":
			boat_t[0][(i, j)] = 0
		elif val == "^":
			boat_t[0][(i, j)] = 1
		elif val == "x":
			obstacle.add((i, j))
		else:
			start = (i, j)

queue = deque([(0, *start)])
visited = set()
while queue:
	t, i, j = queue.popleft()
	if (i, j) in obstacle:
		continue
	if len(boat_t) == t:
		boat_t.append({})
		for ((ii, jj), delta) in boat_t[-2].items():
			if delta:
				if ii == 0 or (ii-1, jj) in obstacle:
					boat_t[-1][(ii, jj)] = 0
				else:
					boat_t[-1][(ii-1, jj)] = 1
			else:
				if ii == m-1 or (ii+1, jj) in obstacle:
					boat_t[-1][(ii, jj)] = 1
				else:
					boat_t[-1][(ii+1, jj)] = 0
	if (i, j) in boat_t[-1]:
		continue
	if i == m or i == -1 or j == -1:
		continue
	if j == n:
		print(t)
		break
	if (t, i, j) in visited:
		continue
	visited.add((t, i, j))
	queue.append((t+1, i, j))
	queue.append((t+1, i+1, j))
	queue.append((t+1, i, j+1))
	queue.append((t+1, i-1, j))
	queue.append((t+1, i, j-1))

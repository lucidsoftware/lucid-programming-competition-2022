# Farthest Island
from heapq import heappush, heappop
def solve():
	m, c = map(int, input().split()); input()
	h = []
	for d, cost in enumerate(map(int, input().split())):
		heappush(h, cost)
		if c:
			c -= 1
		else:
			m -= heappop(h)
			if m < 0:
				return d
	return d + 1
print(solve())

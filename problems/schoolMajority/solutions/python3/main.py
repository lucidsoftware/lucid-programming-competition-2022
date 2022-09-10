from sys import stdin, stdout
import heapq

nums = stdin.readline().split()
n = int(nums[0])
m = int(nums[1])
types = int(nums[2])

grid = []
queue = []
counter = {}
heapq.heapify(queue)


class GridQueue:
    def __init__(self, x, y, fish, gen):
        self.generation = gen
        self.x = x
        self.y = y
        self.fish = fish

    def __lt__(self, other):
        if self.generation < other.generation:
            return True
        if self.generation == other.generation and self.fish < other.fish:
            return True
        return False

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", gen: " + str(self.generation) + ", type: " + self.fish


def add_to_queue(fish, x, y, gen):
    heapq.heappush(queue, GridQueue(x, y, fish, gen))
    if fish in counter:
        counter[fish] += 1
    else:
        counter[fish] = 1


def process_curr(current: GridQueue):
    if current.x > 0:
        if grid[current.x - 1][current.y] == '0':
            grid[current.x - 1][current.y] = current.fish
            add_to_queue(current.fish, current.x - 1, current.y, current.generation + 1)
    if current.x < n - 1:
        if grid[current.x + 1][current.y] == '0':
            grid[current.x + 1][current.y] = current.fish
            add_to_queue(current.fish, current.x + 1, current.y, current.generation + 1)
    if current.y > 0:
        if grid[current.x][current.y - 1] == '0':
            grid[current.x][current.y - 1] = current.fish
            add_to_queue(current.fish, current.x, current.y - 1, current.generation + 1)
    if current.y < m - 1:
        if grid[current.x][current.y + 1] == '0':
            grid[current.x][current.y + 1] = current.fish
            add_to_queue(current.fish, current.x, current.y + 1, current.generation + 1)


# read in grid
for i in range(n):
    line = stdin.readline().split()
    grid.append([])
    for j in range(m):
        grid[i].append(line[j])
        if line[j].isalpha():
            add_to_queue(line[j], i, j, 0)

# process heap
while len(queue) > 0:
    curr = heapq.heappop(queue)
    process_curr(curr)

# find max school
maxKey = list(counter.keys())[0]
for key in list(counter.keys()):
    if counter[key] > counter[maxKey]:
        maxKey = key
        
print(maxKey)

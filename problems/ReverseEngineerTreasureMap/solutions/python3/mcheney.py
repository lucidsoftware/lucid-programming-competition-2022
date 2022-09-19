import math

N = int(input())
x, y = [int(ea) for ea in input()[1:-1].split(',')]
mx, my = 0, 0
for n in range(N - 2):
    line = input().split(' ')
    direction = line[1]
    paces = int(line[2])
    if direction == 'north':
        my += paces
    if direction == 'south':
        my -= paces
    if direction == 'east':
        mx += paces
    if direction == 'west':
        mx -= paces

distToMapEnd = math.sqrt(mx**2 + my**2)
distToTreasure = math.sqrt(x**2 + y**2)
print(round(distToTreasure / distToMapEnd))

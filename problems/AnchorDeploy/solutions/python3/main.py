D, N = [int(ea) for ea in input().split(' ')]

REEF = 'reef'
ROCKS = 'rocks'
PI = 3.14159265  # can actually be any value


def circleArea(radius):
    return PI * (radius ** 2)


totalArea = circleArea(D)
clearArea = circleArea(D)
retryArea = 0
failArea = 0

for n in range(N):
    line = input().split(' ')
    t = line[0]
    x = int(line[1])  # unused
    y = int(line[2])  # unused
    r = int(line[3])

    obstacleArea = circleArea(r)
    clearArea -= obstacleArea
    if t == REEF:
        # fail
        failArea += obstacleArea
    else: # t == ROCKS
        # retry
        retryArea += obstacleArea

probFailure1 = failArea / totalArea  # probability of failing after first throw
probRetry1 = retryArea / totalArea
probFailure2 = probFailure1 + probRetry1 * probFailure1  # probability of having failed by second throw
probRetry2 = probRetry1 * probRetry1
probFailure3 = probFailure2 + probRetry2 * ((failArea + retryArea) / totalArea)  # probability of having failed by third throw

print('{:.3f}'.format(probFailure3))

nums = [int(ea) for ea in input().split(' ')]

oxygenLeft = nums[0]

dead = False
for ea in nums[1:-1]:
    oxygenLeft -= 1
    oxygenLeft = max(oxygenLeft, ea)
    if oxygenLeft == 0:
        dead = True
        break

if dead:
    print(0)
else:
    print(1)

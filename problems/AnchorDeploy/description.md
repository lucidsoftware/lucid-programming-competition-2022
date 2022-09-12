You are sailing the high seas with your captain and crew, enjoying the salt air and even saltier rations. It's the end of the day, and the captain has charged you with deploying the ship's anchor. You must do a good job, or else you will be thrown overboard. There are different obstacles on the ocean floor that might cause the anchor deployment to fail. You want to know how likely it is you'll be thrown overboard.

When you deploy the anchor, it will land in a random point within `d` distance of the ship (the length of the anchor's chain). It is equally likely that the anchor will land at any point in the circle formed by the chain. For this problem, consider the size of the ship to be negligible. In other words, it is possible for the anchor to deploy directly beneath the ship, even if this might not be realistic. After you deploy the anchor, there are 3 possible outcomes:
1. The anchor lands in a coral reef. It gets stuck, and you are thrown overboard.
2. The anchor lands in a patch of rocks. This will not provide a good anchoring point, so you retract it and try again.
3. The anchor lands on clear ground. This is a successful deployment, and you avoid being thrown overboard.

In addition, the captain has a short temper. If you fail to deploy the anchor 3 times, you will be thrown overboard.

## Input
Input will begin with 2 space separated integers:
- D: the length of the chain. 0 < D <= 1000000
- N: the number of obstacles. 0 < N < 10000

Next will follow N lines. Each line describes an obstacle. The line will consist of the obstacle's type (`reef` or `rocks`), the x and y coordinates of its center, and its radius. For example, the line `reef 2 5 4` means that there is a coral reef at coordinates `(2,5)` with radius of 4.

Any ground not covered by an obstacle is clear ground.

The ship is at coordinates `(0,0)`.

It is guaranteed that all the obstacles will be within the anchor's range. No obstacle will overlap the edge of the anchor's range. No 2 obstacles will overlap.

## Output
Output the probability you will be thrown overboard, rounded to 3 decimal places (i.e. 0.27434 => 0.270). Always print 3 decimal places. For example, 0.5 should be printed as 0.500

## Examples

### Input 0
```
10 3
reef 0 5 4
reef 6 0 4
rocks -5 0 2
```

### Output 0
```
0.33
```
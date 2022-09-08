# Cheapest Cost To Build Bridges
Given a m x n 2D binary matrix which represents a map of 1s land and 0s water, return the minumum cost to connect all the islands with bridges or -1 if it is impossible.

A bridge is a vertical or horizontal path over water between islands with a cost associated with the number of water cells the path traverses. Bridges can cross over the same water cell and this will not effect the length of either bridge.

A island is surrounded by water and formed by connecting adjacent land horizontally or vertically.

## Input
The input will contain the size of the binary matrix on the first line `m n` then `m` lines each containing `n` integers representing cells on the matrix.

```
m n
grid[0][0], grid[0][1], ..., grid[0][n-1]
grid[1][0], grid[1][1], ..., grid[1][n-1]
...
grid[m-1][0], grid[m-1][1], ... grid[m-1][n-1
```

## Output
The output will be a single integer representing the minimum total cost to connect all islands.

## Constraints
$1 \leq m, n \leq 1000$

All values given will be integers.

### Example Input
```
3 3
1 0 1
0 0 0
0 1 1
```

### Example Output
```
2
```

### Explanation
Two bridges each of length one are needed to connect all islands on the given graph
```
1 - 1
0 0 |
0 1 1
```

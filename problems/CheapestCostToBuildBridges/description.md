# Cheapest Cost To Build Bridges
Given a `m` x `n` 2D binary matrix that represents a map of 1s land and 0s water, return the minimum cost to connect all the islands with bridges or `-1` if it is impossible.

A bridge is a vertical or horizontal path over water between islands with a cost associated with the number of water cells the path traverses. In other words, all bridges are straight, and can only run either north-south or east-west.

An island is surrounded by water and formed by connecting adjacent land horizontally or vertically.

## Input
The first line will contain two integers `m` and `n` representing the size of the matrix `m` x `n`.
The next `m` lines will each contain `n` integers representing the values of the matrix.

```
m n
grid[0][0], grid[0][1], ..., grid[0][n-1]
grid[1][0], grid[1][1], ..., grid[1][n-1]
...
grid[m-1][0], grid[m-1][1], ... grid[m-1][n-1]
```

## Output
The output will be a single integer representing the minimum total cost to connect all islands, or -1 if impossible.

## Constraints
1 <= m, n <= 1000

m and n will be integers

grid[i][j] will be 0 or 1

## Examples

### Example Input 0
```
3 3
1 0 1
0 0 0
0 1 1
```

### Example Output 0
```
2
```

### Explanation 0
Two bridges each of length one are needed to connect all islands
```
1 - 1
0 0 |
0 1 1
```


### Example Input 1
```
3 3
1 0 1
0 0 0
0 1 0
```

### Example Output 1
```
-1
```

### Explanation 1
Only two of the islands can be connected.
```
1 - 1
0 0 0
0 1 0
```


### Example Input 2
```
3 3
1 1 0
1 0 1
0 1 0
```

### Example Output 2
```
2
```

### Explanation 2
Two bridges each of length one are needed to connect all islands
```
1 1 0
1 + 1
0 1 0
```


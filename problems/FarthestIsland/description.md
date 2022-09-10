# Farthest Island
John is on vacation and plans to travel to as many islands as he can. To take the ferry from island `i` to island `i + 1` he needs to pay `costs[i]` amount of money or use 1 coupon. Once a coupon has been used it _cannot_ be reused. John starts at island `0` with `m` money and `c` coupons. What is the furthest island John can travel to?

## Input
The first line will contain two integers `m` and `c` representing the amount of money & coupons respectively.
The second line will contain an integer `s` representing the size of the `costs` array.
The third line will contain `s` integers representing the values in the `costs` array.

```
10 4
7
7 2 4 1 1 4 8
```

## Output
The output should be a single integer representing the furthest island John can reach with optimal usage of money & coupons.

## Constraints
$m$ and $c$ will be non-negative integers
$1  \leq s \leq  100000$
$costs[i]$ will be a positive integer

## Examples

### Example Input 1
```
5 2
5
10 20 3 2 1
```

### Example Output 1
```
4
```

### Explanation 1
```
John travels from island 0 to island 1 by using 1 coupon.
John travels from island 1 to island 2 by using 1 coupon.
John travels from island 2 to island 3 by paying $3.
John travels from island 3 to island 4 by paying $2.

John has $0 left and 0 coupons left. The furthest island he can travel to is island 4.
```

### Example Input 2
```
7 1
6
2 4 6 2 1 1
```

### Example Output 2
```
3
```

### Explanation 2
```
John travels from island 0 to island 1 by paying $2.
John travels from island 1 to island 2 by paying $4.
John travels from island 2 to island 3 by using 1 coupon.

John has $1 left and 0 coupons left. John cannot travel to the next island since it costs $2.
The furthest island he can travel to is island 3.
```

### Example Input 3
```
1 1
4
6 2 2 10
```

### Example Output 3
```
1
```

### Explanation 3
```
John travels from island 0 to island 1 by using 1 coupon.

John has $1 left and 0 coupons left. John cannot travel to the next island since it costs $2.
The furthest island he can travel to is island 1.
```

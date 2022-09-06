# Reef Populations

Cora l'Rief is an aspiring marine biotechnologist, and she is convinced that there are patterns to be found in the various shoals of fish that live along the Great Barrier Reef. Since the reef is fairly linear, the populations of these shoals can be represented as a one-dimensional array of integers. Cora has several ranges that she would like to analyze by finding the [bitwise exclusive or](https://en.wikipedia.org/wiki/Exclusive_or#Bitwise_operation) (`^` or `XOR` in most languages) of the population sizes contained in those ranges. Can you respond to Cora's queries?

## Input
The first line of input consists of two integers `n q`, where `n` is the number of shoals in the reef, and `q` is the number of queries.

The second line of input consists of `n` space-separated integers, representing the shoal sizes along the reef.

The next `q` lines are of the form `x y`, where `x` is the 1-indexed position of the first reef in the query range, and `y` is the position of the last reef in the query range (inclusive).

```
n q
a1 a2 ... an
x1 y1
x2 y2
...
xq yq
```

## Output
For each query, output the XOR of the shoal population sizes in the query range. Each query result should be on a separate line.

```
r1
r2
...
rq
```

## Constraints
$0 < n \leq 1000000$

$0 \leq q \leq 1000000$

$0 \leq a \leq 2^{31} - 1$

$1 \leq x \leq y \leq n$

All values given will be integers.

### Example Input
```
5 3
6 0 10 8 8
1 3
4 4
3 5
```

### Example Output
```
12
8
10
```

### Explanation
$6 \text{\textasciicircum} 0 \text{\textasciicircum} 10 = 0110_{2} \text{\textasciicircum} 0000_{2} \text{\textasciicircum} 1010_{2} = 12$

$8 = 0100_{2} = 8$

$10 \text{\textasciicircum} 8 \text{\textasciicircum} 8 = 1010_{2} \text{\textasciicircum} 1000_{2} \text{\textasciicircum} 1000_{2} = 10$
## Problem Statement

You’re building a wall of a sandcastle and you only have one size of bucket. Your friend suggests a configuration of a wall given as an array of integers, where `wall[i]` is how tall the wall is at index `i`. You know that for the sandcastle to be stable, the maximum difference between any section of the wall and the 3 sections adjacent to it on either side can be at most 4 buckets. In other words, no section of the wall can be more than 4 buckets taller than the 3 sections on either side (**consider the ends to be 0 buckets tall**). 

Is your friend’s suggestion a stable sandcastle?


## Input
The input will be formatted in the following way:

```
n
2 1 3 4 2
```

Where **n is the length of the array**.

## Output
Output the string "True" if the sandcastle is stable (as defined above) or "False" otherwise

```
True
```

```
False
```

## Constraints
```
0 < n <= 10000
0 <= wall[i] <= 10000
```

### Example input #1:
```
5
1 2 3 4 5
```

### Example output #1:
```
True
 ```

### Example input #2:
```
10
3 2 3 4 6 5 1 5 5 5
 ```

### Example output #2:
```
False
```
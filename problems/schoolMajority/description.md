## Problem Statement

After a big extinction event, the ocean has been reduced to only a few types of fish. Which ones will rise to the top to dominate the seas?

You will be given a grid representing the ocean, each tile can begin with either **0**, meaning open ocean, **1**, meaning land, or a letter of the alphabet, which designates a type of fish.

Your job is to repopulate the ocean, and determine which species of fish will create the largest school. Start with the initial colonies and expand outward in simultaneous generations until all available spaces (open ocean, not previously claimed by any fish type) have been claimed and then return the species with the largest population.

Fish expand in cardinal directions, not diagonally. Each fish type is a letter, so if two fish would expand to the same square in the same generation, the letter that comes first in the alphabet will expand to that position. i.e. **A** would win the battle with **C** to expand to the open square.

## Input
The input will be formatted in the following way:

```
n m x
0  0  0  ...  0
0  1  0  ...  B
...
```

Where **n is the length of the array, m is the width of the array, and x is the number of fish types**.

## Output
Output the name of the fish with most fish after all possible expansions have occurred.

```
A
```

```
B
```

## Constraints
```
0 < n <= 50
0 < m <= 50
0 < x <= 5
All inputs will give a majority species (No ties)
```

### Example input #1:
```
5 5 2
0  0  0  1  0
0  1  0  0  B
0  0  0  1  0
0  A  0  0  0
0  0  0  0  1
```

### Example output #1:
```
A
 ```

### Example input #2:
```
10 9 2
0  0  1  0  0  0  0  1  B
1  0  0  B  B  0  0  1  0
0  0  1  0  0  0  0  1  0
A  0  0  0  0  0  0  1  0
0  0  0  1  0  0  0  1  0
0  0  1  0  0  0  0  1  0
1  0  0  B  0  0  0  1  0
0  0  1  0  0  0  0  1  0
A  0  0  0  0  0  0  0  0
0  0  0  1  0  0  A  1  0
 ```

### Example output #2:
```
B
```

# Reverse Engineering Poseidon's Treasure Maps

## Description

You seek to recover the many chests of treasure Poseidon buried on an island. Fortunately, you have all of Poseidon's treasure maps. Unfortunately, the instructions on his maps are all in terms of "paces" and---having never seen how tall Poseidon is---you have no idea how long his pace might be. Eventually, you find one chest with nothing more than a metal detector. You then realize that by measuring the treasure's location relative to the center of the island (which Poseidon used as the origin point of all his maps), you can work out the actual length of Poseidon's pace.

## Input

- The first line will be one positive integer $n$ indicating the total number of lines of input
- The second line will be one ordered pair `(<x>,<y>)` representing the location of the known treasure; where `<x>` and `<y>` are integers, east is the positive $x$ direction, and north is the positive $y$ direction
- The remaining $n-2$ lines will be instructions of the form `Walk <direction> 1 pace` or `Walk <direction> <p> paces`; where `<direction>` is one of `north`, `south`, `east`, or `west` and `<p>` is an integer number of paces

## Output

Output $l$, the integer length of Poseidon's pace in meters. Do not output any decimal points, commas, or similar.

## Constraints

- $3 \le n \le 10000$
- At least one of $x$ and $y$ will be non-zero
- $1 \le p \le 10000$
- $1 \le l \le 100000$

## Examples

### Input 0
```
3
(0,100000)
Walk north 1 pace
```

### Output 0
```
100000
```

### Input 1
```
4
(16,12)
Walk east 4 paces
Walk north 3 paces
```

### Output 1
```
4
```
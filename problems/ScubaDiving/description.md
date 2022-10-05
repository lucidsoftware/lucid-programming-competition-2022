# Scuba Diving

You are on a Scuba Diving trip with friends and going deeper and deeper into the ocean, you get pretty deep when you remember that eventually you need to go back up, you happen to be an atrocious planner 
and didn't think of the going back up to the surface "part". Luckily for you, your friends have been leaving an oxygen tank every step of the way up to the surface (good planners). Knowing this, you must figure out if you can make it to the top of the surface with the provided oxygen tanks. You can only carry one oxygen tank at a time.

## Input
There is one line of input which is an array of integers (seperated by spaces. e.g "4 3 2 1 0 2"). Each integer represents an oxygen tank at a location, index 0 is the bottom of the ocean, the end index is the surface. It requires 1 unit of oxygen to go from (x) to (x+1). You may choose at each index to keep your current oxygen tank, or replace it with the new oxygen tank. You start at index 0.


## Output
Write 1 (true) or 0 (false) to the stdout representing if you can make it to the surface or not (with oxygen).

## Constraints

1 <= nums.length <= 10^{4}

0 <= nums[x] <= 10^{9}

All values given will be integers.

### Example Input 1
```
4 3 2 1 0 1
```

### Example Output 1
```
0
```

### Explanation
You will always arrive at index 4 and can not reach the surface.

### Example Input 2
```
5 0 0 0 2 0 2
```

### Example Output 2
```
1
```

### Explanation
Take oxygen tank at index 0, take oxygen tank at index 4, reach the surface.

### Example Input 3
```
1 0
```

### Example Output 3
```
0
```

### Explanation
Take oxygen tank at index 0, reach the surface by traveling one unit.

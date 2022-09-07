# Storm Predictor

You want to take your boat fishing, but if there's a storm coming, you don't want to get stuck out at sea. If you see storm cloud patterns, notice the wind blowing south, feel an air pressure change, or notice that the animals have gone silent, those are all indicators that a storm may be coming. If only one or two of those things happen, you'll still go out, but if three or four of them happen, you'll stay in for the day to be safe. 

Given an input like:

```
Storm clouds: false
South winds: true
Air pressure change: true
Silent animals: false
```

Print out either:
```
Go fishing!
```
or
```
Wait for the storm to pass.
```

## Input

You will receive four lines of input. Each line will always have the storm indicators exactly as written below, followed by a boolean (either "true" or "false"). A valid example is:

```
Storm clouds: false
South winds: true
Air pressure change: true
Silent animals: false
```

## Output

As output, you will indicate whether it is safe to go fishing, with the exact message:

```
Go fishing!
```
or
```
Wait for the storm to pass.
```

## Constraints

- The input will always follow the described format.
- One of the two expected outputs is always correct.

## Examples

### Input 0

```
Storm clouds: false
South winds: true
Air pressure change: true
Silent animals: false
```

### Output 0

```
Go fishing!
```

### Input 1

```
Storm clouds: true
South winds: true
Air pressure change: true
Silent animals: true
```

### Output 1

```
Wait for the storm to pass.
```
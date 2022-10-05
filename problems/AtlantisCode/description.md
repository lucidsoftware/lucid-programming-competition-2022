# Atlantis Code
## Description
During an expedition, an ocean explorer has discovered an ancient Seagate Hard Drive burried among the ruins of Atlantis. In order to access the contents of the precious hard drive (which undoubtedly contains priceless NFTs) the explorer must decrypt it using a numeric password that has been crudely transcribed on an ancient Atlantian Post-It Note. The code says the following: Each key contains the characters A, B, and C only and evaluates to an integer. Starting at score = 0, for each individual A, you add 1 to the count. For each individual B, you add 2 to the score. For each AB pair, you add 4 to the score *instead of their individual values*. However, for each C, you subtract the square of the number of AB pairs that are present in the entire code string.

## Input
The input will come from two lines. The first line is the number of characters in the code (an integer). The second line is the code itself.


## Output
The score as an integer value

## Constraints
The number of characters in the code will always be 1 <= n <= 10000

## Examples
### Input 1
```
9
AAABBBCAB
```
### Output 1 and Explanation
```
10
```

#### Explanation
A   A   AB  B   B   C   AB
1 + 1 + 4 + 2 + 2 - 4 + 4 = 10. Note that we subtract 4 because there are 2 AB pairs in the entire code: 2^2 = 4.

### Input 2
```
12
CABCABCAAABB
```
### Output 2
```
-11
```

#### Explanation
 C   AB  C   AB  C   A   A   AB  B
-9 + 4 - 9 + 4 - 9 + 1 + 1 + 4 + 2 = -11
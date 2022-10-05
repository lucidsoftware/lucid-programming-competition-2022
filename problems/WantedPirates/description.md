# Wanted Pirates
A collection of government officials are intending to establish bounties for the world's most notorious pirates. Because their budget for bounties is limited, they want to start with only the most widely wanted pirates, so they intend to issue bounties only for those pirates that are wanted globally.

Given a list of pirates that are wanted in each country, determine the list of pirates that are wanted in every country.

## Input

```
Number of Countries
Line
Line
Line
...
```
The number of countries is an integer between 2 and 1000000

Line
```
N, <list of names>
```
A line is a comma separated list, and starts with the name of the country. Each other item on the list is the name of a pirate

The number of pirates on a line can be any number from 1 to 2000

## Output
The list of pirates wanted in every country, sorted lexicographically.
Each name should appear on its own line

```
Blackbeard
Jack Sparrow
Wang Zhi
```

## Example Inputs and Output

**Input 1:**
```
3
Barbados,Charlotte Lin-Lin,Sir Francis Drake,Jack Sparrow,Captain Kidd
Singapore,Wang Zhi,Captain Kidd,Jack Sparrow
Great Britain,Sir Francis Drake,Charlotte Lin-Lin,Captain Kidd,Jack Sparrow,Blackbeard
```

**Output 1:**
```
Captain Kidd
Jack Sparrow
```

**Input 2:**
```
6
Jamaica,Christopher Moody,Charlotte Lin-Lin,Sayyida Al Hurda,Monkey D. Luffy,Cool Runnings
France,Han Solo,Arthur Pendragon,Monkey D. Luffy,Jack Sparrow,Christopher Moody,Sayyida Al Hurda,Blackbeard
Dressrosa,Monkey D. Luffy,Edward Newgate,Christopher Moody,Jack Sparrow,Sayyida Al Hurda,Arthur Pendragon
Antigua,Long John Silvers,Blackbeard,Christopher Moody,Monkey D. Luffy,William Kidd,Sayyida Al Hurda,Wang Zhi,Stede Bonnet,Anne Bonny,Gol D. Roger
Saudi Arabia,Sayyida Al Hurda,Monkey D. Luffy,Lawrence of Arabia,Christopher Moody
Coruscant,Han Solo,Christopher Moody,Sayyida Al Hurda,Brownbeard,Barbosa,Monkey D. Luffy
```

**Output 2:**
```
Christopher Moody
Monkey D. Luffy
Sayyida Al Hurda
```

## Constraints

The number of pirates on a line is between 1 and 2000
The number of countries is between 2 and 1000000
# Fish Survival
## Description
Marine biologists tracking fish populations have discovered that there are two types of events that affect populations. If the biologists track these events they can keep track of fish populations without counting everything, but they need someone to process the events to determine the final population. The two events are listed below:

1. The fish population grows at a rate X. 
2. The fish population creates groups of size Y to defend against predator attacks. Each group grows until it is size Y and then another group forms. Any group that doesn’t reach size Y is not sufficiently large to scare off predators, and all of the fish in that group are eaten.

Given a starting population and a series of events, the biologists need you to determine the population of fish after the events have occurred and return it as a number.

## Input
Input will be formatted as follows:
* The first line will be two numbers
  * The first number will represent the number of starting fish
  * The second number will represent the number of events that will occur
* The following lines until the end of input will represent one of the possible events
  * Growth events will be sent as “G <number>” where <number> is the number of new fish
  * Predator events will be sent as “P <number>” where <number> is the size of each fish group


## Output
* A single integer representing the ending population of fish

## Constraints
0 <= Total fish population at any time <= 2,000,000,000

0 <= Fish population growth <= 2,000,000

1 <= Group size <= 200,000

1 <= Lines of input <= 100,000

## Examples
### Input 1
```
10 3
G 7
P 4
G 4
```
### Output 1
```
20
```

### Input 2
```
18 6
P 5
P 6
G 15
G 15
P 10
G 20
```
### Output 2
```
60
```

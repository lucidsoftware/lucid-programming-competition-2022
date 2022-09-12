# Scuba Do
## Description
You run a marine salvage company. Each job that comes in has a different set of required pieces of equipment that you would need to complete the job. Given a list of jobs and the tools that they require, return the list of jobs you have the equipment to complete in alphabetical order.

## Input
Input will be provided in the following format:

```
<toolNames>
<numTools>
<jobs>
<jobName>
<requiredToolNames>
<requiredNumTools>
```

* The first two lines will each contain a list
    * The first list, `toolNames`, is a comma separated list of strings that represent the tools that you have on hand
    * The second list, `numTools`, is a comma separated list of integers that represent the amount of each tool that you own
    * Where `toolNames[n]` -> `numTools[n]`
        * So if `toolNames` is ['oxygen tanks', 'bolt cutters'] and `numTools` is [4, 2], then you would have 4 oxygen tanks and 2 bolt cutters
* The next line, `jobs`, will be an integer that denotes the number of available jobs
* The lines that proceed will come in as follows
    * `jobName` - a string that represents the name of the job
    * `requiredToolNames` - a comma separated  list of strings that represent the tools required to complete this job
    * `requiredNumTools` - a comma separated list of integers that represent the number of each tool required to complete this job
    * Where `requiredToolNames[n]` -> `requiredNumTools[n]`
        * So if `requiredToolNames` is ['wet suit', 'shark cage'] and `numTools` is [3, 2], then you would need 3 wet suits and 2 shark cages to complete this job

## Output
Your output should be all of the job names that you are able to complete with your tools. Each job should be on it's own line and they should be listed in case-insensitive alphabetical order.

## Constraints

* 1 <= toolNames, numTools, requiredToolNames, requiredNumTools <= 50
* 1 <= numTools[i], requiredNumTools[i] <= 10
* 1 <= jobs <= 100,000


## Examples

### Input 1
```
'oxygen tanks', 'shark cage', 'rope', 'goggles'
2, 1, 1, 10
2
A
'bolt cutters', 'goggles'
3, 1
B
'rope', 'shark cage', 'oxygen tanks'
1, 1, 2
```

### Output 1
B


### Input 2
```
'oxygen tanks', 'bolt cutters', 'wet suits'
4, 2, 5
3
A
'bolt cutters'
1
B
'rope', 'wet suits', 'bolt cutters'
2, 1, 2
C
'oxygen tanks', 'wet suits'
3, 3
```

### Output 2
A
C
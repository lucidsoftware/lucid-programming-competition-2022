# Fish Counting
## Description
You are the owner of sushi resturant and have a large delivery of fish arriving tommorrow.\
Unfortunately, the list of what you are recieving has become horribly scrambled, and you would like to figure out how many of each fish is arriving tomorrow.

## Input
The input is a newline terminated string that contains the scrambled names of the fish arriving tomorrow.\
The number of times a fish's name occurs within the scrambled string is how many of that fish is arriving tomorrow.


Each fish contained within the scrambled string is one of six fish from the set below:\
[halibut, mackerel, salmon, snapper, squid, tuna]\
The above set denotes what fish may appear within the string, but not all fish will necessarily appear in a given string.


For example, the unscrambled string "salmonsalmonsnapper" contains two salmon and one snapper. Meaning that two salmon and one snapper are arriving tomorrow.\
However, the input for this problem will be scrambled and instead appear as something like "rpempsaasalnnnoomls", which is the same two salmon one snapper string as above, but scrambled.


## Output
Each fish and how many times it occurs within the scrambled string will be printed out in alphabetical order, each on it's own line.\
The name of the fish and the number of occurances will be seperated by a colon with no whitespace in between.\
Each line is terminated by a newline, including the last line.

### Output format:

halibut:#\
mackerel:#\
salmon:#\
snapper:#\
squid:#\
tuna:#

## Constraints
Each input will contain a scrambled string consiting n fish where 1 <= n <=10000

## Examples
### Input 1
macqslerekuid

### Output 1
halibut:0\
mackerel:1\
salmon:0\
snapper:0\
squid:1\
tuna:0

### Input 2
haltdiuqsreppansnomlasnomlaslerekcamtubiuna

### Output 2
halibut:1\
mackerel:1\
salmon:2\
snapper:1\
squid:1\
tuna:1

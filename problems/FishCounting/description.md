# Fish Counting
## Description
You are the owner of sushi restaurant and have a large delivery of fish arriving tomorrow.\
Unfortunately, the list of what you are receiving has become horribly scrambled, and you would like to figure out how many of each fish is arriving tomorrow.

## Input
The input is a newline terminated string that contains the scrambled names of the fish arriving tomorrow.\
The number of times a fish's name occurs within the scrambled string is how many of that fish is arriving tomorrow.\
Additionally, all of the characters in the scrambled string correspond to a full fish name, in other words, you can assume that there are no extra or missing characters in the input.


Each fish contained within the scrambled string is one of six fish from the set below:\
[halibut, mackerel, salmon, snapper, squid, tuna]\
The above set denotes what fish may appear within the string, but not all fish will necessarily appear in a given string.


For example, the unscrambled string "salmonsalmonsnapper" contains two salmon and one snapper. Meaning that two salmon and one snapper are arriving tomorrow.\
However, the input for this problem will be scrambled and instead appear as something like "rpempsaasalnnnoomls", which is the same two salmon one snapper string as above, but scrambled.

## Output
Each fish and how many times it occurs within the scrambled string will be printed out in alphabetical order, each on it's own line.\
The name of the fish and the number of occurrences will be separated by a colon with no whitespace in between.\
Each line is terminated by a newline, including the last line.\
This output format ensures that each input has a single valid output, if you are having trouble with your output, make sure that the last line ends in a newline.

### Output format:

halibut:#\
mackerel:#\
salmon:#\
snapper:#\
squid:#\
tuna:#

## Constraints
Each input will contain a scrambled string consisting n fish where 1 <= n <=10000

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

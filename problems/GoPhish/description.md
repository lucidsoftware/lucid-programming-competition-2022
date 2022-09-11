# Go Phish

You are in charge of operating the email server for a popular snorkeling shop.
Recently, employees have been receiving a lot of emails that look like they came from the owner of the shop or a fellow employee, but in fact were sent by a malicious botnet.
Luckily, you've noticed that the botnet always misspells the name of the shop employees by exactly one letter.

For example, if an employee were named `Alice Sandcastle`, then the botnet might spell this name as `Alice Sandkastle`. Alternately, the botnet might add or remove exactly one letter, as in `Alic Sandcastle` or `Alice Sandecastle`.
You are tired of these emails, but want to be careful to not filter too aggressively and miss important communications from a customer.

Given a list of real employee names, and then a list of names that came from the email server, write a script that can classify each name into three categories: `EMPLOYEE`, `BOT`, or `CUSTOMER`.
A name is an `EMPLOYEE` if it shows up on the employee list and is not misspelled in anyway.
A name is a `BOT` if it differs from an employee name by exactly one character (either a replacement, deletion, or addition).
A name is a `CUSTOMER` if it differs from an employee name by more than one character.

**Important**: Names are _not_ case sensitive, meaning that you should consider `Alice` to be the exact same name as `alice`. For the purposes of this classifier, spaces are also considered non-essential characters, meaning that `Alice Sandcastle` is the same name as `AliceSandcastle`.


# Input
The input format consists of a positive integer on a single line representing the number of employees working for the shop, followed by the name of each employee on a separate line.
Following the employee list, you will receive another integer on a single line representing the number of names to classify, followed by the list of names, each on a line.
```
<number of employees>
<employee 0>
<employee 1>
...
<employee x>
<number of names to classify>
<name 0>
<name 1>
...
<name y>
```

# Output
The expected output is the classification of each name, in the exact order they were given in the input. Your output should consist of the strings `EMPLOYEE`, `BOT`, or `CUSTOMER` on each line, in uppercase.
```
<EMPLOYEE | BOT | CUSTOMER>
<EMPLOYEE | BOT | CUSTOMER>
...
<EMPLOYEE | BOT | CUSTOMER>
```

# Constraints
* The number of employees will always be between 1 and 100 (inclusive)
* The number of names to classify will be between 1 and 100,000 (inclusive)
* The length of a name will always be between 2 and 30 (inclusive)
* Names of employees and names to classify will only consist of the upper and lowercase letters A-Z and may contain a single space in the middle.
* Names are *not* case or space sensitive, meaning that, for purposes of classification, you should consider `alicesandcastle` to be the exact same name as `Alice Sandcastle`.


# Example 0
## Input 0
```
2
Alice Sandcastle
Taylor Umbrella
3
Alice Sandcastle
Tayler Umbrella
Mariana Trench
```
## Output 0
```
EMPLOYEE
BOT
CUSTOMER
```
# Example 1
## Input 1
```
3
Olivia Orca
Isaac Irrawaddy
Hector Commerson
6
oliviaOrca
isac iriwaddy
HelctorCommerson
Isac Irrawaddy
Olivia Orcas
Olavia Orcash
```
##Output
```
EMPLOYEE
CUSTOMER
BOT
```



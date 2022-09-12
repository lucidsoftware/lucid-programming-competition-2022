from sys import stdin, stdout

codeLength = int(stdin.readline().strip())
code = stdin.readline().strip()
countDict = {}

abScore = 4
aScore = 1
bScore = 2

currentScore = 0
numberOfCs = 0

# Strip all the ABs from the string
newCodeString = code.replace("AB", "")

# We can now calculate the number of AB pairs by taking the string length difference
numberOfABPairs = (codeLength - len(newCodeString)) // 2
squaredABPairs = numberOfABPairs ** 2

# And add them to the score
currentScore += 4 * numberOfABPairs

# Now go through the simplified code (with AB pairs removed and run the calculations)

for i in range(len(newCodeString)):
    currentChar = newCodeString[i]
    
    if currentChar == 'A':
        currentScore += aScore
    elif currentChar == 'B':
        currentScore += bScore
    elif currentChar == 'C':
        currentScore -= squaredABPairs
        
print(currentScore)
stdout.flush()

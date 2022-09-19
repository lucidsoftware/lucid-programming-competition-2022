
def runEvent(numFish, eventType, eventNum):
    if (eventType == "G"): # Growth event
        numFish += eventNum
    elif (eventType == "P"): # Predator event
        fishEaten = numFish % eventNum
        numFish -= fishEaten
    return numFish

def calculateFish():
    startingNums = input().split(" ")
    numFish = int(startingNums[0])
    numEvents = int(startingNums[1])
    for i in range(numEvents):
        eventParts = input().split(" ")
        eventType = eventParts[0]
        eventNum = int(eventParts[1])
        numFish = runEvent(numFish, eventType, eventNum)
    return numFish

fishCount = calculateFish()
print(fishCount)
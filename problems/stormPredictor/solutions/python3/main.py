import sys

def isSafeToFish():
    trueCount = 0

    for line in range(4):
        boolean = input().split(": ")[1]
        if (boolean == "true"):
            trueCount += 1

    return trueCount <= 2

def printResult(isSafe):
    if (isSafe):
        print("Go fishing!")
    else:
        print("Wait for the storm to pass.")

isSafe = isSafeToFish()
printResult(isSafe)
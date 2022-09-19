import heapq

M, C = [int(ea) for ea in input().split(' ')]
S = int(input())
costs = [int(ea) for ea in input().split(' ')]

bought = []


def maxHeapPush(heap, value):
    heapq.heappush(heap, -value)


def maxHeapPop(heap):
    if len(heap) == 0:
        return 0
    return -heapq.heappop(heap)


i = 0
while (M > 0 or C > 0) and i < len(costs):
    nextCost = costs[i]
    # If you have enough money, just buy ticket
    if M >= nextCost:
        M -= nextCost
        maxHeapPush(bought, nextCost)
        i += 1
        continue
    if C == 0:
        # No more coupons or money
        break
    # If you don't have enough money, consider using coupon on most expensive previous buy
    prevBuy = maxHeapPop(bought)
    M += prevBuy
    C -= 1
    if prevBuy > nextCost:
        # Previous buy was more expensive. Use coupon it instead.
        maxHeapPush(bought, nextCost)
        M -= nextCost
    else:
        # Previous buy was cheaper than current buy. Use coupon on current buy.
        maxHeapPush(bought, prevBuy)
        M -= prevBuy
    i += 1

print(i)

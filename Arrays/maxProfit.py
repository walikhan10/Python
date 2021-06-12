

def maxProfit(prices):

    # brute force solution not fast!!!!!!!
    arr = []

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):

            if(prices[j] - prices[i] > 0):
                arr.append(prices[j] - prices[i])
    if not arr:
        return 0
    else:
        return max(arr)


def maxProfit2(prices):
    maxP = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxP:
                maxP = profit
    return maxP


# test = [7, 1, 5, 3, 6, 4]

# print(maxProfit2(test))


# two pointer solution
def maxProfit3(prices):
    l, r = 0, 1

    maxP = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


test = [7, 1, 5, 3, 6, 4, 0, 8]

print(maxProfit3(test))

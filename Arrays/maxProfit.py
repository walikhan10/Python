

def maxProfit(prices):

    arr = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):

            if(prices[j] - prices[i] > 0):
                arr.append(prices[j] - prices[i])
    if not arr:
        return 0
    else:
        return max(arr)


test = [7, 6, 4, 3, 1]

print(maxProfit(test))

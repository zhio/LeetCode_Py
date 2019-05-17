def maxProfit(prices):
    profit = 0
    i = 0
    while i <len(prices)-1:
        minimum = prices[i]
        j = i+1
        if prices[i]>=prices[j]:
            minimum = min(prices[j],minimum)
            i+=1
        else:
            while j<=len(prices)-1:
                if j == len(prices)-1:
                    profit +=prices[j]-minimum
                    return profit
                elif prices[j]<=prices[j+1]:
                    j+=1
                else:
                    profit+=prices[j]-minimum
                    i = j+1
                    break

    return profit

def maxProfit2(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit += prices[i]- prices[i-1]

    return profit

#profit=（3-1)+(5-3)+(6-2)+(3-1)=3-1+5-3+(6-2)+(3-1)=(5-1)+(6-2)+(3-1)

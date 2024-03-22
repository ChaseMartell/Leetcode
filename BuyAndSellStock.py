#Calculates the lostest buying day, and highest selling day to get the maximum amount of profit.
def buyAndSellStock(prices):
    maxProfit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[right] > prices[left]:
            maxProfit = max(maxProfit, prices[right]-prices[left])
        else:
            left = right
        right += 1

    return maxProfit

def main():
    print(buyAndSellStock([3,4,5,6,7,2,3,8,1]))
    print(f'The maximum profit is: {buyAndSellStock([4,5,6,7,8,2,3,4])}')

if __name__ == "__main__":
    main()
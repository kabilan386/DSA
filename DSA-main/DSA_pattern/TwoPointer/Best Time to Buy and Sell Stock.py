def buyandsellprice(prices):
    profit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[right] > prices[left]:
            max_profit = prices[right] - prices[left] 
            profit = max(max_profit,profit)
        else:
            left = right
        
        right += 1

    


print(buyandsellprice([7,4,5,3,6,4]))
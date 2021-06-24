"""
Problem description:
    1) Given an array of price of stock and where prices[i] is the price of a given stock on ith day.
    2) Find out the maximum profit that can be made by buying a stock from a day and selling it on the future day  

"""


def buy_and_sell_stock(prices):
    prices_len = len(prices)
    max_profit = 0
    if prices_len < 1:
        return 0
    else:
        min_price = min(prices, default=0)
        min_price_index = prices.index(min_price)
        
        for i in range(min_price_index+1, prices_len):
            diff = abs(min_price - prices[i])
            if diff > max_profit:
                max_profit = diff
        
    return max_profit


# print(buy_and_sell_stock([7,1,5,3,6,4]))
print(buy_and_sell_stock([2,4,1]))
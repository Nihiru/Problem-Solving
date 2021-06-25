"""
Problem description:
    1) Given an array of price of stock and where prices[i] is the price of a given stock on ith day.
    2) Find out the maximum profit that can be made by buying a stock from a day and selling it on the future day  

"""


def buy_and_sell_stock_I(prices):
    prices_len = len(prices)
    max_profit = 0
    if prices_len < 1:
        return 0
    else:
        """
        The approach I took here is to select the least price to buy stock and this does not match the requirements/description specfied
        Thereby, commenting the code.
        Refer the Problem description to understand better
        """
        # min_price = min(prices, default=0)
        # min_price_index = prices.index(min_price)
        
        # for i in range(min_price_index+1, prices_len):
        #     diff = abs(min_price - prices[i])
        #     if diff > max_profit:
        #         max_profit = diff

        """ 
        Below approach is considered based on 
        1) starting with a stock and comparing it with previous set stock to identify the minimum stock available. Just to make a profit
        2) Complexity
            1) Time Complexity: O(N) where N is the number of elements in the array to be traversed
            2) Space Complexity: O(1) where temporary variables are used for computation
        """
        min_stock_price = float('inf')
        for price in prices:
            min_stock_price = min(price, min_stock_price)
            profit = price - min_stock_price
            max_profit = max(max_profit, profit)


    return max_profit


# print(buy_and_sell_stock([7,1,5,3,6,4]))
print(buy_and_sell_stock_I([2,4,1]))
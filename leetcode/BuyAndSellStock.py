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
        1) Time Complexity: O(N) where N is the number of elements in the array to be traversed
        2) Space Complexity: O(1) where temporary variables are used for computation
        """
        min_stock_price = float('inf')
        for price in prices:
            """to find a stock with minimum value,
               checking if the current stock i.e, price is minimum stock by comparing to the previous stock value
            """
            min_stock_price = min(price, min_stock_price)
            """
            if I consider that current stock of the day is minimum and I buy it and sell it on the current day itself
                then I'm assuming I'm getting zero profit
            as I move on to the next day, again I'm checking if the current day stock is minimum or not
            if yes
                then consider that as my purchasing stock (even though I'm analysing and not purchasing)
            else
                compute previous day stock value with current day stock value and check the profit.
            """
            profit = price - min_stock_price
            """
            making sure we're achieving maximum profit
            """
            max_profit = max(max_profit, profit)

    return max_profit


"""

Dynamic Programming
1) Dimensions of a problem projects the states computed after each transition 
2) State defines a position after a computation
3) A Transition defines an set of operations for states to be altered and these states may be a new one or replacing an existing one.

"""


def buy_and_sell_stock_II(prices):
    best_with_stock = float('-inf')
    best_without_stock = 0
    for price in prices:
        """
        Below approach follows Dynamic Programming
        1) A new state for best_with_stock and best_without_stock is computed based on its previous state
        2) functionalities of best_with_stock
            1) Responsible for holding stocks with least prices.
            2) Identify the minimum stock by comparing it to the previous days stock
            3) Assuming that I'm going to buy current days stock and selling it on the next day and should make a profit and not a loss
        3) best_without_stock specifies 
            1) It is used to calculate the maximum profit by checking the previous stock with current stock.
        """
        best_with_stock = max(best_with_stock, best_without_stock - price)
        best_without_stock = max(best_without_stock, best_with_stock + price)

    return best_without_stock


def buy_and_sell_stock_III(prices):
    """Performing at most two transactions

    Args:
        prices (Array[int]): [prices of stock on each day]
    """


print(buy_and_sell_stock_I([2, 4, 1]))
"""
To understand better using different scenarios
"""
print(buy_and_sell_stock_II([7, 1, 5, 4, 6, 3]))
print(buy_and_sell_stock_II([7, 6, 5, 4, 3, 2, 1]))

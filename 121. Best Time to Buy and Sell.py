"""
Leetcode Problem 121
Best Time to Buy and Sell
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0: 
        return 0 
    
    min_price = prices[0]
    max_profit = 0 
    
    for price in prices: 
        min_price = min(min_price, price)
        profit = price-min_price
        max_profit = max(max_profit, profit)
    
    return max_profit

stock_prices = [7,5,2,1,3]
print(f"Max Profit is: {maxProfit(stock_prices)}")
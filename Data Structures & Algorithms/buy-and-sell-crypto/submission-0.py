class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') #we are assuming min price as infinity
        max_profit = 0

        for price in prices: #loop, goes throught the prices array
            if price<min_price: #if current price is less that min_price
                min_price = price #update the min_price to current price and its the best time to buy stocks

            elif price - min_price > max_profit: #current price - min_price is greater thamn max profit
                max_profit = price - min_price #we update max profut and its the best time to sell the stock

        return max_profit
        
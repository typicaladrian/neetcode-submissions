class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            We are given an integer array prices where prices[i] is the price of NeetCoin
            on the ith day.

            We need to choose a SINGLE day to buy one Neetcoin and a different day
            in the future to sell it.

            We need to choose a different day in the future to sell it.

            WE CAN RETURN 0 IF A PROFITABLE TRANSACTION IS NOT POSSIBLE
        '''

        # A naive solution of course is to create every combination of buy/sell days
        # The problem with this is that it results in a time completity of O(n^2)

        # We can do better!

        # Lets create two pointers to keep track of our buy day and our sell days

        # Now, the trick to this is that at a sell point of i, we need to find the
        # minimum value to buy at from the values at the left of our sell point i

        '''
            We iterate through our entire array, with the current index being where we
            plan to sell.

            We also need to keep track of the minimum value to the left of the current index.
            We can do this by storing a running minimum value.

            We also need to keep track of the maximum running profit, so we store that as well.
        '''
        currBuy = prices[0]
        maxProfit = 0

        for price in prices:
            currBuy = min(currBuy, price)
            maxProfit = max(maxProfit, price - currBuy)
       
        return maxProfit
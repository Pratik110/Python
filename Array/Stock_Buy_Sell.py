Link = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
Description = "You are given an array prices where prices[i] is the price of a given stock on the ith day." \
              "You want to maximize your profit by choosing a single day to buy one stock and choosing a " \
              "different day in the future to sell that stock. Return the maximum profit you can achieve " \
              "from this transaction. If you cannot achieve any profit, return 0."
Example = "Input: prices = [7,1,5,3,6,4]" \
          "Output: 5" \
          "Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5." \
          "Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell."

prices = [7,1,5,3,6,4]

# Approach 1

class Solution1:
    def maxProfit(self, prices):
        minm = prices[0]
        profit = 0
        for i in prices:
            currProf = 0
            if i < minm:
                minm = i
            else:
                currProf = i - minm
                if currProf > profit:
                    profit = currProf
        return profit
print("Maximum profit is ", Solution1().maxProfit(prices))

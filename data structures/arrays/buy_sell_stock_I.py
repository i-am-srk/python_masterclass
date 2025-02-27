from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, profit = prices[0], 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price < buy_price:
                buy_price = current_price
            elif current_price - buy_price > profit:
                profit = current_price - buy_price

        return profit

obj = Solution()
nums = [7,1,5,3,6,4]
print(f"ans : {obj.maxProfit(nums)}")
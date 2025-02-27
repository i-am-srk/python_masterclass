from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                profit += nums[i]-nums[i-1]

        return profit

obj = Solution()
nums = [7,1,5,3,6,4]
print(f"result: {obj.maxProfit(nums)}")
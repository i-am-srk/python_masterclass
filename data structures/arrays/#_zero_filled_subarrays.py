from typing import List


class Solution:
    def zeroFilledSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        for num in nums:
            if num == 0:
                l += 1
            else:
                l = 0

            ans += l

        return ans


obj = Solution()
nums = [1,3,0,0,2,0,0,4]
print(f"answer: {obj.zeroFilledSubarrays(nums)}")
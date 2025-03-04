from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                swap(nums, i, nums[i]-1)

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
            
        return len(nums)+1
                

obj = Solution()
nums = [3,4,-1,1]
print(f"result: {obj.firstMissingPositive(nums)}")
from collections import deque

class Solution():
    """
    time - O(n)
    space - O(n)
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix, suffix = [1], deque([1]) 
        for i in range(1, len(nums)):
            prefix.append(nums[i-1]*prefix[i-1])
            suffix.appendleft(nums[len(nums)-i]*suffix[0])

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        
        return ans

obj = Solution()
nums = [1,2,3,4]
print(f"inference: {obj.productExceptSelf(nums)}")
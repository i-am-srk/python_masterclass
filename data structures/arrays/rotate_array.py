from typing import List


class Solution():
    def rotateArray(self, nums: List[int], k: int) -> None:
        """
        intution: reverseing any segment twice brings it back to its original state

        time - O(n)
        space - O(1)
        """
        n = len(nums)
        k %= n
        nums[:] = reversed(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])



obj = Solution()
nums = [1,2,3,4,5,6,7]
print(f"inference: {obj.rotateArray(nums, 3)}")
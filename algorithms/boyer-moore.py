class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        T - O(n) with 2 linear passes
        S - O(1)
        """

        candidate, count = None, 0

        # find the majority candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        # validate occurences
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        return None

        
obj = Solution()
nums = [3,2,3]
print(f"ans : {obj.majorityElement(nums)}")  

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        T - O(n)
        S - O(1)
        """

        k=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k
    
obj = Solution()
nums = [1,1,1,2,2]
print(f"ans : {obj.removeDuplicates(nums)} | nums : {nums}")
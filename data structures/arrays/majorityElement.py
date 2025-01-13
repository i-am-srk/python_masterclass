class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for k in freq:
            if freq[k] > len(nums)/2:
                return k
            
obj = Solution()
nums = [2,2,1,1,1,2,2]
print(f"ans : {obj.majorityElement(nums)}")
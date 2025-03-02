import math
from typing import List


class Solution:
    def increasingTripletSubsequence(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False

obj =  Solution()
nums = [2,1,5,0,4,6]
print(f"result : {obj.increasingTripletSubsequence(nums)}")
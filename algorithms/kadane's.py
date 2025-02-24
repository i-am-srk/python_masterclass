# maximum subarray

from typing import List
import sys


class Kadane(object):
    def variant_1(self, nums: List[int]) -> int:
        """
        return the maximum subarray sum

        time - O(n)
        space - O(1)
        """
        maxi = -sys.maxsize-1
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            
            if sum > maxi:
                maxi = sum

            if sum < 0:
                sum = 0

        return maxi
    
    def variant_2(self, nums: List[int]) -> int:
        """
        along side the max sum, print that subarray

        same time and space complexity as above
        """
        maxi = -sys.maxsize-1
        sum = 0
        start = 0
        arrStart, arrEnd = -1, -1

        for i in range(len(nums)):
            if sum == 0:
                start = i
            
            sum += nums[i]

            if sum > maxi:
                maxi = sum
                arrStart = start
                arrEnd = i

            if sum < 0:
                sum = 0

        print(f"maximum sum subarray: [", end="")
        for i in range(arrStart, arrEnd+1):
            print(nums[i], end="" if i == arrEnd else ",")
        print(end="]\n")

        return maxi
        
obj = Kadane()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(f"maximum sum : {obj.variant_1(nums)}")
print(f"maximum sum : {obj.variant_2(nums)}")  
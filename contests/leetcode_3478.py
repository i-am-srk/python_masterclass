from typing import List
import heapq


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        res = [0]*n
        last = -1
        lasttotal = 0

        heap1 = [[val, idx] for idx, val in enumerate(nums1)]
        heapq.heapify(heap1)

        heap2 = []
        curtotal = 0

        while heap1:
            val, idx = heapq.heappop(heap1)

            if val == last:
                last = val
                res[idx] = lasttotal
                curtotal += nums2[idx]
                heapq.heappush(heap2, nums2[idx])

            else:
                last = val

                while heap2 and len(heap2) > k:
                    v = heapq.heappop(heap2)
                    curtotal -= v

                res[idx] = curtotal
                lasttotal = curtotal
                curtotal += nums2[idx]
                heapq.heappush(heap2, nums2[idx])

        return res


obj =Solution()
nums1 = [18,11,24,9,10,11,7,29,16]
nums2 = [28,26,27,4,2,19,23,1,2]
k = 1
print(f"answer: {obj.findMaxSum(nums1, nums2, k)}")
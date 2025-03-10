from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break

        result = 0
        for basket in baskets:
            if basket != 0:
                result += 1

        return result


obj = Solution()
fruits = [3,6,1]
baskets = [6,4,7]
print(f"answer: {obj.numOfUnplacedFruits(fruits, baskets)}")
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return s == s[::-1]

obj = Solution()
s = "A man, a plan, a canal: Panama"
print(f"result: {obj.isPalindrome(s)}")
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return True if sp == len(s) else False

obj = Solution()
s = "abc"
t = "ahbgdc"
print(f"result: {obj.isSubsequence(s, t)}")
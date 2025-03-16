class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        
        idx, d = 0, 1
        answer = ["" for _ in range(numRows)]

        for char in s:
            answer[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        return "".join(answer)

obj = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(f"result: {obj.convert(s, numRows)}")
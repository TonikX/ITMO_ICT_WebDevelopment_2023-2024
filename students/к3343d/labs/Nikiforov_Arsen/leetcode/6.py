# https://leetcode.com/problems/string-to-integer-atoi/submissions/
class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign, i = 1, 0
        if s[0] in ["-", "+"]:
            sign = -1 if s[0] == "-" else 1
            i = 1

        number = 0
        for j in range(i, len(s)):
            if not s[j].isdigit():
                break
            number = number * 10 + int(s[j])

        return max(-2**31, min(sign * number, 2**31 - 1))

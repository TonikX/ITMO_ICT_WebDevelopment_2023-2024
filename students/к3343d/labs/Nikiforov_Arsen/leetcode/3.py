# https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s or len(s) < 1:
            return ""

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            longer = len1 if len(len1) > len(len2) else len2
            if len(longer) > end - start:
                start, end = i - ((len(longer) - 1) // 2), i + (len(longer) // 2)

        return s[start:end + 1]

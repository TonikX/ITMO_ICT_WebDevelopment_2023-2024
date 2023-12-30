# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s):
        start, maxLength = 0, 0
        charIndexMap = {}

        for i in range(len(s)):
            if s[i] in charIndexMap and charIndexMap[s[i]] >= start:
                start = charIndexMap[s[i]] + 1
            charIndexMap[s[i]] = i
            maxLength = max(maxLength, i - start + 1)

        return maxLength

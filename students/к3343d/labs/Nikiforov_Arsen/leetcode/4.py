# https://leetcode.com/problems/zigzag-conversion/submissions/
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index, step = 0, 1

        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(result)

# https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x):
        sign = [1,-1][x < 0]
        reversed_x = sign * int(str(abs(x))[::-1])

        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0

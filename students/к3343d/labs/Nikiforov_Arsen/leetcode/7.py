# https://leetcode.com/problems/palindrome-number/submissions/
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reversed_x, original_x = 0, x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return original_x == reversed_x

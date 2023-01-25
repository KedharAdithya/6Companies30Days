class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n):
            if not self.isPalindrome(self.convertToBase(n, base)):
                return False
        return True

    def convertToBase(self, n, base):
        """Convert an integer to a string representation in a given base"""
        if n == 0:
            return "0"
        digits = []
        while n:
            digits.append(int(n % base))
            n //= base
        return "".join(str(d) for d in digits[::-1])

    def isPalindrome(self, s):
        """Check if a string is a palindrome"""
        return s == s[::-1]
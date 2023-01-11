class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k > 0:
            step, first, last = 0, curr, curr + 1
            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10
            if k >= step:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr
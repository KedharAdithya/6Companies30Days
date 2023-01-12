class Solution:
    def findIntegers(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])
        ans = 0
        last_seen = 0
        for i in range(29, -1, -1):
            if (n >> i) & 1:
                ans += f[i]
                if last_seen: 
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans + 1
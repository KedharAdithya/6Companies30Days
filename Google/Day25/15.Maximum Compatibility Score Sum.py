class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        a, b = [], []
        for student in students:
            x = 0
            for i in range(m):
                x += student[i] << (m - i - 1)
            a.append(x)
        for mentor in mentors:
            x = 0
            for i in range(m):
                x += mentor[i] << (m - i - 1)
            b.append(x)
        dp = {}
        def solve(i, mask):
            if i >= n:
                return 0
            if mask in dp:
                return dp[mask]
            ans = 0
            for k in range(n):
                if mask & (1 << k):
                    new_mask = mask ^ (1 << k)
                    current_ans = 0
                    for x in range(m):
                        if (a[i] & (1 << x)) == (b[k] & (1 << x)):
                            current_ans += 1
                    ans = max(ans, current_ans + solve(i + 1, new_mask))
            dp[mask] = ans
            return ans
        mask = (1 << n) - 1
        return solve(0, mask)
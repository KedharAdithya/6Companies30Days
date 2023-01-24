class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, dot_count, curr_ip, ans):
            if dot_count == 3:
                if is_valid(s):
                    ans.append(curr_ip + s)
                return

            for i in range(1, 4):
                if i <= len(s):
                    if is_valid(s[:i]):
                        dfs(s[i:], dot_count + 1, curr_ip + s[:i] + ".", ans)

        def is_valid(s):
            return 0 < len(s) <= 3 and (s[0] != '0' if len(s) > 1 else True) and int(s) <= 255

        ans = []
        dfs(s, 0, "", ans)
        return ans
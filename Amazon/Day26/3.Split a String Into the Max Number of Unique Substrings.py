class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # set to keep track of used substrings
        used_substrings = set()
        # variable to store the maximum number of unique substrings
        max_count = 0
        
        def backtrack(s, count):
            nonlocal max_count
            # if the entire string has been split
            if not s:
                # update max_count if count is greater than current max_count
                max_count = max(max_count, count)
                return
            # iterate through substrings of s
            for i in range(1, len(s) + 1):
                substring = s[:i]
                if substring not in used_substrings:
                    used_substrings.add(substring)
                    backtrack(s[i:], count + 1)
                    used_substrings.remove(substring)
                    
        backtrack(s, 0)
        return max_count
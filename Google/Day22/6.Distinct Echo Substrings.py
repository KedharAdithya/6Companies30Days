class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        ans = 0
        s = set()
        for i in range(1, n):
            # check all substrings from i//2+1 to i
            for j in range(i//2+1, i+1):
                # get the length of substring to check
                l = i+1-j
                temp = text[j-l:j]
                # check if the substring is equal to the concatenation of itself
                if temp == text[j:i+1]:
                    s.add(temp)
        # return the number of distinct substrings
        return len(s)
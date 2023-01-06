class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        count = 0
        
        last_a = -1
        last_b = -1
        last_c = -1
        
        for i, c in enumerate(s):
            
            if c == 'a':
                last_a = i
            elif c == 'b':
                last_b = i
            elif c == 'c':
                last_c = i
          
            if last_a != -1 and last_b != -1 and last_c != -1:
                count += 1 + min(last_a, last_b, last_c)
        return count
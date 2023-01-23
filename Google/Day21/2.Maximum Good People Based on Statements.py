# approach 1 using dictionaries
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        res, n, good, bad = 0, len(statements), defaultdict(int), defaultdict(int) 
        for i in range(n): 
            for j in range(n):
                if statements[i][j] == 1:
                    good[i] = good[i] | (1 << j)    
                elif statements[i][j] == 0:
                    bad[i] = bad[i] | (1 << j) 
        for mask in range(1 << n):  
            good_count = 0
            for a in range(n):
                if (1 << a) & mask:
                    good_count += 1
                    if not(mask & good[a] == good[a] and mask & bad[a] ^ bad[a] == bad[a]): 
                        break
            else: 
                res = max(res, good_count)
        return res




# approach 2 using lists
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        good, bad = [0]*n, [0]*n
        for i in range(n): 
            for j in range(n):
                if statements[i][j] == 1:
                    good[i] |= (1 << j)    
                elif statements[i][j] == 0:
                    bad[i] |= (1 << j) 
        res = 0
        for mask in range(1 << n):  
            good_count = 0
            for a in range(n):
                if (1 << a) & mask:
                    good_count += 1
                    if not(mask & good[a] == good[a] and mask & bad[a] ^ bad[a] == bad[a]): 
                        break
            else: 
                res = max(res, good_count)
        return res
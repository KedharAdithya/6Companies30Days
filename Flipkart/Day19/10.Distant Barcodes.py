class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
      
        n = len(barcodes)
        count = collections.Counter(barcodes)
        ans = [0] * n
        i = 0
        for code, _ in count.most_common():
            for _ in range(count[code]):
                ans[i] = code
                i += 2
                if i >= n:
                    i = 1
                    
        return ans

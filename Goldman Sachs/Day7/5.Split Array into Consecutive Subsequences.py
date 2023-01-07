class Solution: 
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        freqs = Counter(nums)
        tails = Counter()
        for num in nums:			
            if freqs[num] == 0:
                continue				
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num + 1] += 1
            elif freqs[num + 1] > 0 and freqs[num + 2] > 0:
                freqs[num + 1] -= 1
                freqs[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            freqs[num] -= 1
        return True
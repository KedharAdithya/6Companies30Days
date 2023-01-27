class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        self.shuffled = nums.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        random.shuffle(self.shuffled)
        return self.shuffled

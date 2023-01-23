class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_consecutive = 0
        consecutive = 0
        prev = bottom - 1
        for floor in special:
            if prev + 1 < floor:
                max_consecutive = max(max_consecutive, floor - prev - 1)
            prev = floor
        if prev + 1 < top:
            max_consecutive = max(max_consecutive, top - prev)
        return max_consecutive

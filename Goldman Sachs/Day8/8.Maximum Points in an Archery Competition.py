class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_points = 0
        best_choice = [0] * 12
        for mask in range(2**12):
            bob_taken = 0
            bob_points = 0
            choice = [0] * 12
            for j in range(12):
                if ((1<<j) & mask) > 0:
                    bob_taken += aliceArrows[j] + 1
                    bob_points += j
                    choice[j] = aliceArrows[j] + 1
            if bob_taken > numArrows:
                continue
            if bob_points > max_points:
                max_points = bob_points
                choice[0] += numArrows - bob_taken
                best_choice = choice[:]
        return best_choice
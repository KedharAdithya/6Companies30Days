class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9:
            return []
        if n > sum(range(1, 10)):
            return []
        if k == 1:
            if n in range(1, 10):
                return [[n]]
            else:
                return []
        combinations = []
        def backtrack(start, combination, remaining):
            if remaining == 0 and len(combination) == k:
                combinations.append(combination)
                return
            if remaining < 0 or len(combination) > k:
                return
            for i in range(start, 10):
                backtrack(i + 1, combination + [i], remaining - i)
        backtrack(1, [], n)
        return combinations
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j, res, count = 0, 0, 0, collections.Counter()
        for k in range(len(fruits)):
            count[fruits[k]] += 1
            while len(count) >= 3:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            res = max(res, k - i + 1)
        return res

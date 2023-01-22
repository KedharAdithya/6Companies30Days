class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        probability = deque([1 if k <= pts <= n else 0 for pts in range(k, k + maxPts)])    
        current_sum = sum(probability)
        for i in range(k - 1, -1, -1):
            probability.appendleft(current_sum / maxPts)
            current_sum += probability[0] - probability.pop()
        return probability[0]
# approach 1 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# approach 2


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        items = list(count.items())
        items.sort(key=lambda x: (-x[1], x[0]))
        return [i[0] for i in items[:k]]
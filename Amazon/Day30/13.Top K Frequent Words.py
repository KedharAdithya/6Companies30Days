class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        items = list(count.items())
        items.sort(key=lambda x: (-x[1], x[0]))
        return [i[0] for i in items[:k]]

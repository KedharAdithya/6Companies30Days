class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: pos.get(x, 26)))
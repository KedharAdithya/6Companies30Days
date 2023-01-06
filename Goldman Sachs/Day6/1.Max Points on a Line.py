class Solution:
    def maxPoints(self, P: List[List[int]]) -> int:
        L, M, gcd = len(P), 1, math.gcd
        for i,(x1,y1) in enumerate(P):
            s, D = 1, collections.defaultdict(int, {0:0})
            for (x2,y2) in P[i+1:]:
                g = gcd(y2-y1, x2-x1)
                if g == 0:
                    s += 1
                    continue
                m = ((y2-y1)//g, (x2-x1)//g)
                if m[1] == 0: m = (1,0)
                if m[1] < 0: m = (-m[0],-m[1])
                D[m] += 1
            M = max(M, s + max(D.values()))
        return M if P else 0

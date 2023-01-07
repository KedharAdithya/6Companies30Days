class Solution:
    def minimumCardPickup(self, a: List[int]) -> int:
        d=set()
        s={}
        n=len(a)
        for i in range(n):
            if a[i] in s:
                d.add(a[i])
                s[a[i]].append(i)
            else:
                s[a[i]]=[i]
        if len(d)==0:
            return -1
        for i in d:
            for j in range(len(s[i])-1):
                n=min(n,s[i][j+1]-s[i][j])
        return n+1
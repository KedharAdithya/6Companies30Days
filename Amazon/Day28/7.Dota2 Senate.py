class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = [], [] 
        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            if R[0] < D[0]:
                R.append(R[0] + len(senate))
            else:
                D.append(D[0] + len(senate))
            R.pop(0)
            D.pop(0)
        return "Radiant" if R else "Dire"

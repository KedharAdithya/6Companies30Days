class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        def helper(needs):
            if needs in memo: return memo[needs]
            min_price = sum(p*n for p,n in zip(price, needs))
            for offer in special:
                if all(o <= n for o,n in zip(offer[:-1], needs)):
                    updated_needs = tuple(n-o for o,n in zip(offer[:-1], needs))
                    min_price = min(min_price, offer[-1] + helper(updated_needs))
            memo[needs] = min_price
            return min_price
        
        return helper(tuple(needs))
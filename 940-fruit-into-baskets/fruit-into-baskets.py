class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        ml = 0
        h = {};k = 2
        while r < len(fruits):
            h[fruits[r]] = h.get(fruits[r], 0) + 1
            if len(h) > k:
                h[fruits[l]] = h[fruits[l]] - 1 
                if h[fruits[l]] == 0:
                    h.pop(fruits[l])   
                l = l+1
            if len(h) <=k:
                ml = max(ml,r-l+1)
            r = r+1
        return ml
                
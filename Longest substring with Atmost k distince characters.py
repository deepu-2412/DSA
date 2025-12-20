def Longestsubstring(self,s:str,k:int) -> int:
    l = 0
    ml = 0
    h = {}
    while r < len(s):
        h[s[r]] = h.get(s[r],0)+1
        if len(h) > k:
            h[s[l]] = h[s[l]] -1
            if h[s[l]] == 0:
                h.pop(s[l])
            l = l+1
        if len(h) <=k:
            ml = max(ml,r-l+1)
        r = r+1
    return ml

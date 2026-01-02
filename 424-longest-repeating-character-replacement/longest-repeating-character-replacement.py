class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0;r=0;ml=0;mf=0
        c = [0]*26
        while r<len(s):
            c[ord(s[r])-ord('A')]+=1
            mf = max(mf,c[ord(s[r])-ord('A')])

            if (r-l+1) - mf > k:
                c[ord(s[l]) - ord('A')] -=1
                l = l+1
            if (r-l+1)-mf<=k:
                ml = max(ml,r-l+1)
            r = r+1
        return ml 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0;r = 0
        ml = 0
        h = {}
        while r < len(s):
            if s[r] in h:
                if h[s[r]] >= l:
                    l = h[s[r]]+1
            ml = max(ml,r - l + 1)
            h[s[r]] = r
            r +=1
        return ml
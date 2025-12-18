class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0;r = 0
        ml = 0
        h = set()
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            ml = max(ml, r - l + 1)
        return ml
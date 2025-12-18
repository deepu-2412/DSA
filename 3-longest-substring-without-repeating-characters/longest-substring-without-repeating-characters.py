class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(len(s)):
            h = set()
            for j in range(i,len(s)):
                if s[j] in h:
                    break
                h.add(s[j])
                l = max(l,j-i+1)
        return l
        
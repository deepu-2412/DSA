class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(s):
            return False
        elif sorted(s) == sorted(t):
            return True
        return False
        
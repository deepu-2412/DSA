class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z = 0
        lp = 0
        rp = 0; ml = 0
        while rp < len(nums):
            if nums[rp] == 0:
                z = z+1
            if z > k:
                if nums[lp] == 0:
                    z = z - 1
                lp = lp + 1
            if z<=k:
                ml = max(ml,rp-lp+1)
            rp = rp+1
        return ml

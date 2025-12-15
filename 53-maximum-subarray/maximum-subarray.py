class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        m = nums[0]
        for i in range(len(nums)):
            if curr  < 0 :
                curr = 0 
            curr = curr + nums[i]
            m = max(curr,m)
        return m
        
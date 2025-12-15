class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minv = nums[0]
        maxv = nums[0]
        res = maxv
        for i in range(1,len(nums)):
            temp = min( nums[i] , minv*nums[i] , maxv*nums[i] )
            maxv = max( nums[i] , minv*nums[i] , maxv*nums[i] )     
            minv = temp
            res = max(res,maxv)
        return res
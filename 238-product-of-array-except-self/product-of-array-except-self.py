class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        pre = 1
        post = 1
        for i in range(len(nums)):
            l.append(pre)
            pre = nums[i] * pre
        for i in range(len(nums)-1,-1,-1):
            l[i] = l[i] * post
            post = nums[i] * post
        return l
            

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost( nums, goal):
            if goal < 0:
                return 0
            l = 0
            s = 0
            c = 0
            for r in range(len(nums)):
                s += nums[r]%2
                while s > goal:
                    s -= nums[l]%2
                    l += 1
                c += (r - l + 1)
            return c
        return atMost(nums, k) - atMost(nums, k - 1)
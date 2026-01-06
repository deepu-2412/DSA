class Solution:
    def atMost(self, nums, goal):
        if goal < 0:
            return 0

        l = 0
        s = 0
        c = 0

        for r in range(len(nums)):
            s += nums[r]
            while s > goal:
                s -= nums[l]
                l += 1
            c += (r - l + 1)

        return c

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)

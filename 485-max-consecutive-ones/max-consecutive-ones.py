class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = {}
        count = 0
        for i,num in enumerate(nums):
            if num == 1:
                count+=1
            elif num == 0:
                c[i] = count
                count = 0
        c[len(nums)] = count
        return max(c.values())

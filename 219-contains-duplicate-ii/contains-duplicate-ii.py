class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = set()
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            h.add(nums[i])
            if len(h) > k:
                h.remove(nums[i-k])
        return False
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}  # to store key-value pairs 
        for i, num in enumerate(nums):
            if (target - num) in visited:
                return [i , visited[target - num]]
            visited[num] = i
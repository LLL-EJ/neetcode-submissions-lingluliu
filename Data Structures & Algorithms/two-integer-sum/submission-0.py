class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            res = target - num
            if target - num in seen:
                return [seen[res], i]
            seen[num] = i
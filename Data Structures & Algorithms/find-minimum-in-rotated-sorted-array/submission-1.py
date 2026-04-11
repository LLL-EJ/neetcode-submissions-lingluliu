class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]


# Your first approach - tracks min separately
# while l <= r:  # Continues until search space is empty
    # ... logic updates res
    # Eventually l > r, but res has the answer

# Second approach - narrows to single element
# while l < r:   # Continues until search space has 1 element
    # ... logic updates l or r
    # When l == r, nums[l] is the answer
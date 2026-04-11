# height = [1,7,2,5,4,7,3,6]
# index. = [0,1,2,3,4,5,6,7]

# i = 0, j = 7 -> area = (7 - 0) * min(1, 6) = 7
# i = 1, j = 7 -> area = (7 - 1) * min(7, 6) = 36
# i = 1, j = 6 -> area = (6 - 1) * min(7, 3) = 15
# i = 1, j = 5 -> area = (5 - 1) * min(7, 7) = 28
# i = 2, j = 5 -> area = (5 - 2) * min(2, 7) = 6
# i = 3, j = 5 -> area = (5 - 3) * min(5, 7) = 10
# i = 4, j = 5 -> area = (5 - 4) * min(4, 7) = 4

# i, j -> area = (j - i) * min(height[i], height[j]) 
# -> only moving the pointer which has smaller height.


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i, j = 0, len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            max_water = max(max_water, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_water

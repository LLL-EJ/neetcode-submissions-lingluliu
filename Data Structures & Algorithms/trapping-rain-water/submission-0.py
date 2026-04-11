class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = []
        suffix_max = [0] * n # Pre-allocate to fill by index
        
        current_max = 0
        for h in height:
            current_max = max(h, current_max)
            prefix_max.append(current_max)

        current_max = 0
        for i in range(n - 1, -1, -1):
            current_max = max(height[i], current_max)
            suffix_max[i] = current_max  # Fill at the correct index i

        water_area = 0
        for i in range(n):
            water_area += min(prefix_max[i], suffix_max[i]) - height[i]
        return water_area
        
            
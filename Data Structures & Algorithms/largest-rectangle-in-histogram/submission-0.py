class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: (idx, height)
        max_area = 0
        

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (idx - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
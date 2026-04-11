class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair [temp, index]
        res = [0] * len(temperatures)

        for idx, item in enumerate(temperatures):
            while stack and item > stack[-1][0]:
                stack_item, stack_idx = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append((item, idx))
        return res
            

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # store indeces, not values
        result = []
        
        for i, num in enumerate(nums):
            # remove indices outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # remove indices whose values are smaller than current
            while dq and num > nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            # front of deque is always the max of current window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
            
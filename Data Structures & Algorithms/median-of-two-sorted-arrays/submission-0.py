class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        short, long = nums1, nums2

        if len(nums2) < len(nums1):
            short, long = long, short
        
        l, r = 0, len(short) - 1

        while True:
            mshort = (l + r) // 2 # short partition
            mlong = half - mshort - 2 # long partition, minus two index 0 from two lists

            short_left = short[mshort] if mshort >= 0  else float("-infinity")
            short_right = short[mshort + 1] if (mshort + 1) < len(short) else float("infinity")
            long_left = long[mlong] if mlong >= 0 else float("-infinity")
            long_right = long[mlong + 1] if (mlong + 1) < len(long) else float("infinity")

            # condition to find the right partition
            if short_left <= long_right and long_left <= short_right:
                # odd
                if total % 2 == 1:
                    return min(short_right, long_right)
                # even
                return (max(short_left, long_left) + min(short_right, long_right)) / 2
            elif short_left > long_right:
                r = mshort - 1
            else:
                l = mshort + 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, freq in cnt.items():
            buckets[freq].append(num)

        for freq in range(len(buckets) - 1, 0, -1):
            for bucket in buckets[freq]:
                res.append(bucket)
                if len(res) == k:
                    return res
            
# [1,2,2,3,3,3] -> cnt = Counter({1:1, 2:2, 3:3})
# bucket = [[], [1], [2], [3], [], [], []]
# len(res) == k
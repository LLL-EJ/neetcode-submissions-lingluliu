class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # map = {index: [[prefix_product , suffix_product]]}
        d = defaultdict(list)
        products = []

        for idx, num in enumerate(nums):
            prefix_product = math.prod(nums[0: idx])
            suffix_product = math.prod(nums[idx + 1 : ])
            d[idx].append(prefix_product)
            d[idx].append(suffix_product)

        for product_list in d.values():
            products.append(math.prod(product_list))
        
        return products

    

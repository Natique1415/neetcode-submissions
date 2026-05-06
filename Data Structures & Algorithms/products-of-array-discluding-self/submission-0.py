class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (j != i):
                    product *= nums[j]

            ans.append(product)
            product = 1

        return ans
            
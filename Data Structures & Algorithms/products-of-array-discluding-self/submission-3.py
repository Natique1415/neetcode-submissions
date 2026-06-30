class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums_except = [1] * l
        prefix, postfix = 1, 1

        # 1st pass for getting prefix
        for i in range(l):
            nums_except[i] = prefix
            prefix = prefix * nums[i]

        # 2nd pass for getting postfix
        for i in range(l - 1, -1, -1):
            nums_except[i] *= postfix
            postfix *= nums[i]
        
        return nums_except
 
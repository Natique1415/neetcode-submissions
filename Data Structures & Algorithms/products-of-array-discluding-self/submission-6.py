class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        out = [1] * l
        prefix = 1
        postfix = 1

        for i in range(l):
            out[i] = prefix
            prefix = prefix * nums[i]

        for i in range(l - 1, -1, -1):
            out[i] = out[i] * postfix
            postfix = postfix * nums[i]

        return out

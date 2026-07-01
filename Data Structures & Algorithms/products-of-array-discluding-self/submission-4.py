class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix, postfix = 1, 1
        out_arr = [1] * l

        for i in range(l):
            out_arr[i] = prefix
            prefix = prefix * nums[i]

        for i in range(l - 1, -1, -1):
            out_arr[i] = out_arr[i] * postfix
            postfix = postfix * nums[i]

        return out_arr

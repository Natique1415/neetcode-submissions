class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length
        nums_except = []

        # for prefix
        for i in range(length):
            if i == 0:
                prefix[i] = nums[i]

            else:
                prefix[i] = nums[i] * prefix[i - 1]

        # for postfix
        i = length - 1
        while i >= 0:
            if i == length - 1:
                postfix[i] = nums[i]

            else:
                postfix[i] = nums[i] * postfix[i + 1]
            i -= 1

        # finally
        for i in range(length):
            if i == 0:
                nums_except.append(postfix[i + 1])

            elif i == length - 1:
                nums_except.append(prefix[i - 1])
            else:
                nums_except.append(prefix[i - 1] * postfix[i + 1])

        return nums_except

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        while k != 0:
            max_key = next(iter(count))

            for key, val in count.items():
                if val > count[max_key]:
                    max_key = key

            res.append(max_key)
            count.pop(max_key)
            k -= 1

        return res
 
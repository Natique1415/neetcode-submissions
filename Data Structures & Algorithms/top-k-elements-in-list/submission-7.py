class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        counts = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key, val in freq.items():
            counts[val].append(key)


        for i in range(len(nums), 0, -1):
            for j in counts[i]:
                res.append(j)

                if len(res) == k:
                    return res

    
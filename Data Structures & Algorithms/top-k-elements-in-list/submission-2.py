class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_and_count = {}
        ans = []

        for num in nums:
            if num not in num_and_count:
                num_and_count[num] = 1 
            else:
                num_and_count[num] += 1

        num_and_count = dict(sorted(num_and_count.items(), key=lambda item: item[1], reverse=True))

        for ke in list(num_and_count.keys()):
            if k > 0:
                ans.append(ke)

            k = k - 1

        return ans 

        
        
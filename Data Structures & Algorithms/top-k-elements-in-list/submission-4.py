class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_and_count = {}
        ans = []
        i = 0 

        for num in nums:
            if num not in num_and_count:
                num_and_count[num] = 1 
            else:
                num_and_count[num] += 1

        num_and_count = dict(sorted(num_and_count.items(), key=lambda item: item[1], reverse=True))

        while k > 0:
            ans.append(list(num_and_count.keys())[i])
            i += 1 
            k -= 1
            
        return ans 

        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0

        buy = 0
        sell = 0

        for i in range(0, len(prices)):
            buy = prices[i]
            for j in range(i, len(prices)):
                sell = prices[j]

                if sell - buy > max:
                    max = sell - buy

        return max
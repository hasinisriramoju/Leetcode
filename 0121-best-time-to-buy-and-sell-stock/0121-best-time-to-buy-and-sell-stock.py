class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit=0
        leastprice=prices[0]
        for i in range(1,len(prices)):
            leastprice=min(leastprice,prices[i])
        
         
            dayprofit=prices[i]-leastprice
            
            maxprofit=max(maxprofit,dayprofit)

        return maxprofit






        


        
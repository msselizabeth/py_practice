from typing import List

def maxProfit(prices: List[int]) -> int:
    max_diff = 0
    min_day = prices[0] # SC: O(1)
    
    for p in prices: 
        if p < min_day: # TC: O(n)
            min_day = p
        if p - min_day > max_diff:
            max_diff = p - min_day
    return max_diff
    


print(maxProfit([10,1,5,6,7,1]))
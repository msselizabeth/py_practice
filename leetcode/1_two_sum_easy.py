from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen =  {} # O(1)
    result = [] # O(1)
    
    for i, n in enumerate(nums): # O(n)
        complement = target - n # O(1)
        if complement in seen: # O(1) -> 
            result.append(seen[complement]) # O(1)
            result.append(i) # O(1)
            return result   
        seen[n] = i   # O(1) 
        
    

print(twoSum([3,3], 6))
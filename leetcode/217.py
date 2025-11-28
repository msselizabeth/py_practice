from typing import List

# Solution 1
def containsDuplicate(nums: List[int]) -> bool:
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False


# print(f"Res_1: {containsDuplicate([1,2,3,1])}")
# print(f"Res_2: {containsDuplicate([1,6,3,6,8])}")
# print(f"Res_3: {containsDuplicate([1000000000,1000000000,11])}")
# print(f"Res_4: {containsDuplicate([0])}")
print(f"Res_5: {containsDuplicate([1,5,-2,-4,0])}")




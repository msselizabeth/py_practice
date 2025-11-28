def guess_num(nums: list[int], target: int) -> int:
    """
    The function returns an integer representing how many attempts  were made to guess the target number, and the index of target within the list (inclusive).
    """
    attempts = 0
    min = 0
    max = len(nums) - 1

    
    while True:
        mid = (min + max) // 2
        guess = nums[mid]
        
        if guess == target:
            attempts += 1
            return attempts, mid

        if guess > target:
            attempts += 1
            max = mid - 1

        if guess < target:
            min = mid + 1
            attempts += 1


a, m = guess_num([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 12)
print(f"Attempts: {a}")
print(f"Index of target num: {m}")



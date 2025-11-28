

def isPalindrome(x: int) -> bool:
    if(x < 0 or (x % 10 == 0 and x != 0)):
        return False
    rev_half = 0
    
    while rev_half < x:
        rev_half = rev_half * 10 + x % 10
        x = x // 10
        
    if rev_half == x or x == rev_half // 10:
        return True
    return False
    
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(10))
print(isPalindrome(101))
print(isPalindrome(0))
print(isPalindrome(-101))




        
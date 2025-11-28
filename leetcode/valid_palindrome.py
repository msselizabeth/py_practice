import re 

def isPalindrome(s: str) -> bool:
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    reverse_s = cleaned_s[::-1]
    
    print(f"Original: {cleaned_s}")
    print(f"Reverse: {reverse_s}")
    return cleaned_s == reverse_s
    
    
    
    
print(isPalindrome("Was it a car or a cat I saw?"))
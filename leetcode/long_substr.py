

def long_substr(string: str) -> int:
    n = len(string)
    
    if n == 0:
        return 0
    max_l = 0
    left = 0
    chars = set()
    
    for right in range(len(string)):
        current_char = string[right]
        
        
        while current_char in chars:
            char_to_remove = string[left]
            chars.remove(char_to_remove)
            left += 1
        
        chars.add(current_char)
        current_lenght = (right - left) + 1
        max_l = max(max_l, current_lenght) 
        
    return max_l

        
        
res = long_substr("pwwkew")
print("Result:", res)
"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer."""




def romanToInt(s: str) -> int:
    #  roman to int dictionary
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # initial values
    total = 0
    prev_value = 0
    
    # loop throug the reversed string
    for char in reversed(s):
        current_value = roman_dict[char] 
        
        #  if current value less than prev then it's case of (IV, etc) -> we need to substract 
        if current_value < prev_value:
            total -= current_value 
        # if current more than prev -> normal , just add to total  
        else:
            total += current_value
            
        #assigning prev as current after checks for the next iteration    # 
        prev_value = current_value
            
    return total

print(romanToInt("MCMXCIV"))       
      

# def romanToInt(s: str) -> int:
#     s = list(s)
#     integer = 0
#     for idx, item in enumerate(s):
#         integer += roman_dict[item]
        
#         if idx > 0:
#             prev_item = s[idx - 1]
#             if roman_dict[item] > roman_dict[prev_item]:
#                 integer -= roman_dict[prev_item] * 2

        
#     # print(s)
#     print(f"Final: {integer}")


# romanToInt("LVIII")

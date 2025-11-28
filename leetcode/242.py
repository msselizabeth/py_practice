
# ----------------- Solution 1 ------------------------
# ----- Time complexity: O( n*log(n) + m*log(m) ) -----
# ----- Space Complexity: O(n + m) --------------------

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t

# ======================================================


# ----------------- Solution 2 ------------------------
# ----- Time complexity: O(n + m) ---------------------
# ----- Space Complexity: O(1) ------------------------


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return
    counter_S = {}
    counter_T = {}
    for i in range(len(s)- 1):
        counter_S[s[i]] = 1 + counter_S.get(s[i], 0)
        counter_T[t[i]] = 1 + counter_T.get(t[i], 0)
    print(counter_S)    
    return counter_S == counter_T    

s = "maaam" 
t = "aaamm"
print(isAnagram(s, t))
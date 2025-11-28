from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
   strs_dict = {}
   for s in strs:
       soretd_s = "".join(sorted(s))
       s_list = strs_dict.setdefault(soretd_s , [])
       s_list.append(s)

   print(strs_dict) 
   return list(strs_dict.values())
        
 



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
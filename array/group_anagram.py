from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            sorted_str = sorted(str)
            sorted_str = "".join(sorted_str)
            if sorted_str not in dict:
                dict[sorted_str] = []
            dict[sorted_str].append(str)
        out = [*dict.values()]
        return out

from collections import defaultdict
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use the list as default_factory, meaning if the key doesn't exist,
        # then it returns the specified value as default value.
        # list for an empty list
        # ALWAYS ALWAYS ALWAYS USE BUILT-IN DATATYPES
        dict = defaultdict(list)
        
        for str in strs:
            dict["".join(sorted(str))].append(str)
        # Doing this instead of extracting the values yourself
        # speed the code up by like shit ton
        return list(dict.values())        

s = Solution2()
print(s.groupAnagrams(["rat", "tar", "car"]))
    

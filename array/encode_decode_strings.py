from typing import *
'''
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1
Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"

Example 2
Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]

Explanation:

One possible encode method is: "we:;say:;:::;yes"
'''

class Solution:
    def encode(self, strs: List[str]):
        out = ""
        for str in strs:
            out += str.replace(":", "::") + ":;"
        
        return out
    
    def decode(self, str):
        list = []
        collect = ""
        i = 0
        while i < len(str):
            if str[i] == ":":
                if str[i + 1] == ":":
                    collect += ":"
                    i += 1
                else:
                    list.append(collect)
                    collect = ""
                    i += 1
            else:
                collect += str[i]
            i += 1
        return list
    
s = Solution()
print(s.encode(["hi", ":", "lol"]))
print(s.decode(s.encode(["hi", ":", "lol"])))
print(s.encode([":"]))

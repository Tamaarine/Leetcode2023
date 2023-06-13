from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1 = {}
        count2 = {}
        for ch in s:
            if ch not in count1:
                count1[ch] = 0
            count1[ch] += 1
        for ch in t:
            if ch not in count2:
                count2[ch] = 0
            count2[ch] += 1
        for key, value in count1.items():
            if key not in count2 or value != count2[key]:
                return False
        return True

# Apparently Counter class in Python is just super efficient, much more
# efficient than making a counter of your own using dictionary.
# It is optimized for it. So use it for frequently! If possible
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

s = Solution3()
assert s.isAnagram("xaqcrdwcevzfveqwarqfwss" + 'a' * 10000, "freqvwaarscezsqfqxdcwvw" + 'a' * 10000)
assert not s.isAnagram("rat", "cat")
assert s.isAnagram("", "")
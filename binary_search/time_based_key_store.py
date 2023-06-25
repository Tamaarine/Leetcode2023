from typing import *
from collections import *

class TimeMap:

    def __init__(self):
        # The datastructure will be a dictionary, map the key to a list of TUPLE
        # which contains the timestamp and the value
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # To do get, we will do a binary search on the timestamp of the list of tuples mapped
        # from the keys
        lists = self.map[key]
        left = 0
        right = len(lists) - 1
        
        lastMet = -1
        while left <= right:
            mid = (right - left) // 2 + left # This is overflow safe
            
            if lists[mid][0] > timestamp:
                # If the mid list has a bigger timestamp
                # than it is asked, then move right, cuz it is not the right one
                right = mid - 1
            else:
                # If the mid list is less than or equal to the requested timestamp
                # move left up, record mid as lastMet since it could be the only one
                # less than the timestamp
                left = mid + 1
                lastMet = mid
        
        # Then after we exited, we should check if lastMet was found
        if lastMet != -1:
            return lists[lastMet][1]
        # Else then the string was not found with the corresponding key and timestamp
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
s = TimeMap()
s.set("key1", "lmao", 1)
s.set("key1", "lmao1", 2)
s.set("key1", "lmao2", 5)
s.set("key1", "lmao3", 7)
s.set("key1", "lmao4", 10)
print(s.map)
print(s.get("key1", 2))

s2 = TimeMap()
s2.set("key2", "lol", 100)
print(s2.get("key2", 50))
print(s2.get("key2", 150))

s3 = TimeMap()
print(s3.get("key2", 50))
print(s3.get("key2", 150))
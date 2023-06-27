from typing import *
from collections import *

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)
        sandwichCount = Counter(sandwiches)
        
        while len(sandwiches) > 0:
            if studentCount[0] == 0:
                # If the 0 student is done, only 1s left
                if sandwiches[0] == 0:
                    break
            elif studentCount[1] == 0:
                if sandwiches[0] == 1:
                    break
            
            if students[0] == sandwiches[0]:
                popped = students.pop(0)
                sandwiches.pop(0)
                studentCount[popped] -= 1
                sandwichCount[popped] -= 1
            else:
                students.append(students.pop(0))
        return len(students)

class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # No need stacks man
        studentCounts = Counter(students)
        
        for s in sandwiches:
            if studentCounts[s] == 0:
                # No student will be able to consume it no amtter how you rotate
                break
            else:
                studentCounts[s] -= 1
        return studentCounts.total()


s = Solution2()
students = [1,1,1]
sandwiches = [0,0,0]
print(s.countStudents(students, sandwiches))
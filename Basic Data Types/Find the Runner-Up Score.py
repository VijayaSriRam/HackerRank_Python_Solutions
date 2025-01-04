'''
Question Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Question      : Arithmetic Operators
Difficulty    : Easy
Skills        : Python (Basic)
Sub Domain    : Basic Data Types
Language Used : Python 3
'''

#Version-1:
n = int(input())
arr = map(int, input().split())

scores1 = list(arr)
scores1.sort()

scores2 = scores1

runner_up_score = 0

for i in range(len(scores2)):
    if scores2[i] < max(scores2):
        runner_up_score = scores2[i]

print(runner_up_score)

#Time Complexity: O(n²)
#   Converting map to list: O(n)
#   Sorting the list: O(n log n)
#   Finding runner-up: O(n) * O(n) for max() in loop = O(n²)
#   Overall: O(n²) due to the nested max() call
#Space Complexity: O(n)
#   Storing the list: O(n)


#Version-2:
'''
n = int(input())
arr = map(int, input().split())

try:
    scores = sorted(set(arr), reverse=True)
    if len(scores) < 2:
        print("Single participant. There is no runner-up")
    else:
        print(scores[1])
except Exception as e:
    print(f"Error occurred: {e}")
'''

# Time Complexity: O(n log n)
#   Converting map to set: O(n)
#   Sorting: O(n log n)
#   Accessing element: O(1)
# Space Complexity: O(n)
#   Set storage: O(n)
#   Sorted list: O(n)

#Version-1 doesn't handle all edge cases.
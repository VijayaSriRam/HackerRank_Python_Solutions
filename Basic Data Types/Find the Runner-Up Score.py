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

#Time Complexity: O(n^2)
#Space Complexity: O(n)
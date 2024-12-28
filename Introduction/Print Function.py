'''
Question Link : https://www.hackerrank.com/challenges/python-print/problem
Question      : Print Function
Difficulty    : Easy
Skills        : Python (Basic)
Sub Domain    : Introduction
Language Used : Python 3
'''

#Version-1:
n = int(input())
result = ''
for i in range(1, n+1):
    result += str(i)

print(result)

#Time Complexity = O(n^2)
#Space Complexity = O(n)

#Version-2:
'''
n = int(input())
result = ''.join(str(i) for i in range(1, n+1))
print(result)
'''

#Time Complexity = O(n)
#Space Complexity = O(n)

'''
In V-1: Loop runs n times and new string is created every time it concatinates.
In V-2: Loop runs n times, but the result is printed only once at the final string concatination.

Future Work:
    Can modify the code further to resolve issues with edge cases based on the constraints.
'''
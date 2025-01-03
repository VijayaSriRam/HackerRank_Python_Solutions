'''
Question Link : https://www.hackerrank.com/challenges/write-a-function/problem
Question      : Write A Function
Difficulty    : Medium
Skills        : Python(Basic)
Sub Domain    : Introduction
Language Used : Python 3
'''

#Version-1:
def is_leap(year):
    leap = False
    
    if year %400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    
    return leap

#Time Complexity = O(1)
#Space Complexity = O(1)

#Version-2:
'''
def is_leap(year):
    leap = False

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    return leap

'''
#Time Complexity = O(1)
#Space Complexity = O(1)

'''
Future Work:
    Can modify the code further to resolve issues with edge cases based on the constraints.
'''
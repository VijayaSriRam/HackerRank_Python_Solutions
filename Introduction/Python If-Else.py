'''
Question Link : https://www.hackerrank.com/challenges/py-if-else/problem
Question      : Python If-Else
Difficulty    : Easy
Skills        : Python (Basic)
Sub Domain    : Introduction
Language Used : Python 3
'''

n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif (n % 2 == 0) and 2 <= n <= 5:
    print("Not Weird")
elif (n % 2 == 0) and 6 <= n <= 20:
    print("Weird")
elif (n % 2 == 0) and n > 20:
    print("Not Weird")

#Time Complexity = O(1)
#Space Complexity = O(1)

'''
Edge Cases:
    Although the code works, it's better to modify the code further using the try-except statement
    based on the constraints specified.
'''

'''
Question Link : https://www.hackerrank.com/challenges/list-comprehensions/problem
Question      : List Comprehensions
Difficulty    : Easy
Skills        : Python (Basic)
Sub Domain    : Basic Data Types
Language Used : Python 3
'''

#Version-1:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)

'''
#Breakdown of the above code using loops:

ele_list = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i+j+k != n:
                value = [i, j, k]
                
                ele_list.append(value)
                
print(ele_list)
'''

#Time Complexity: O(x+1 * y+1 * z+1)
    # First loop runs (x+1) times
    # For each i, second loop runs (y+1) times
    # For each i and j, third loop runs (z+1) times
#Space Complexity: O(x * y * z)
    # Each combination creates a new list of 3 integers
    # Maximum number of combinations = (x+1) * (y+1) * (z+1)
# Pattern: The repeated or systematic way in which somethiong takes place.
# Few example of pattern shapes:
# 1. Simple Number Triangle Pattern.
# 2. Inverted Pyramid Triangle of Numbers
# 3. Half Pyramid of Numbers.
# 4. Inverted Pyramid of Descending Numbers.
# 5. Inverted Pyramid of Same Digit.
# 6. Reverse Pyramid of Numbers.

# Patterns are made using simple loops, they are applications of nested loops.

# Activity 1: Write a program to demonstrate a right angle triangle pattern.
# Activity 2: Write a progeam to demonstrate a Floyd triangle pattern.
# Activity 3: Write a program to demonstrate the numbers in a diamond pattern.

# Answer 1: 
# *
# * *  
# * * *
# * * * *

# A pair of father and son, both are working in a single field.

#A1
# rows=4
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# #A2
# rows=int(input("Enter the number of rows:"))
# number=1
# print("Floyd's Triangle:")
# for i in range(1,rows+1):
#     for j in range(1,i+1): 
#         print(number, end=" ")
#         number+=1
#     print()



# Example for dry run:

# for i in range(1,10,2): #i=1, i<10 True , # i=3, 3<10 True 
#     print(i)

# Output
# 1
# 3
# 5
# 7
# 9


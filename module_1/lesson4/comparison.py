#Comparison operators in python: The comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison. The comparison operators in python are:
#1. Equal to (==): This operator checks if the values of two operands are equal or not. If they are equal, it returns True, otherwise it returns False.
#2 Not equal to (!=): This operator checks if the values of two operands are not equal. If they are not equal, it returns True, otherwise it returns False.
#3. Greater than (>): This operator checks if the value of the left operand is greater than the value of the right operand. If it is, it returns True, otherwise it returns False.
#4. Less than (<): This operator checks if the value of the left operand is less than the value of the right operand. If it is, it returns True, otherwise it returns False.
#5. Greater than or equal to (>=): This operator checks if the value of the left operand is greater than or equal to the value of the right operand. If it is, it returns True, otherwise it returns False.
#6. Less than or equal to (<=): This operator checks if the value of the left operand is less than or equal to the value of the right operand. If it is, it returns True, otherwise it returns False.   

#Activity: Write a program to calculate the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes needed for a given withdrawal amount.
# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.

# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.

# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.

#Activity:

Amount=int(input("Enter the total withdrawal Amount:"))
note_1=Amount//100
remainder_1=Amount%100
note_2=remainder_1//50
remainder_2=remainder_1%50
note_3=remainder_2//10
print("Number of 100 ruppee notes:", note_1)
print("Number of 50 ruppee notes:", note_2)
print("Number of 10 ruppee notes:", note_3)

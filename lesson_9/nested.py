# Concept of nesting: . Nesting occurs when one statement, function, loop or structure is placed inside another.
# Example: Nested if
# i = 13

# if (i == 13):
#     if (i < 15):
#         print("i is smaller than 15")
#     if (i < 13):
#         print("i is smaller than 13 too")
#     else:
#         print("i is greater than 12 and smaller than 15")

# example of nested if-else:

# n = int(input("enter a number: ")) #67

# if n == 0:
#     print("number is zero")
# else:
#     if n > 0:
#         print("number is positive")
#     else:
#         print("number is negative")

# ACTIVITIES: 


# A1:
# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
#    (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
#    - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
#    a) Ask for the student’s attendance percentage and store it in `atten`.
#    b) If `atten` is 75 or more:
#       - Print "Allowed"
#    c) Else:
#       - Print "Not allowed"


# A2:
# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.

# 2) Use if–elif–else to decide the cost based on `units`:
#    - If `units` is less than 50:
#      Set `amount` as units × 2.60 and set `surcharge` as 25.
#    - Else if `units` is 100 or less:
#      Set `amount` as (cost for first 50 units) + (remaining units × 3.25)
#      Set `surcharge` as 35.
#    - Else if `units` is 200 or less:
#      Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)
#      Set `surcharge` as 45.
#    - Else (units more than 200):
#      Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)
#      Set `surcharge` as 75.

# 3) Calculate the final bill:
#    total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places.


# A3:
# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"


#A2
units=int(input("enter the number of units consumed: "))
if units<50:
    amount=units*2.60
    surcharge=25

elif units<100:
    amount=(50*2.60)+(units-50)*3.25
    
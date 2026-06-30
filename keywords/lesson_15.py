# KEYWORD:
# Return:
#  This statement is used to end the execution of a function call.
#  It returns the result to the caller. 
#  The statements after return are not executed.
#  The return statement cannot be outside of a function.

# Example 1:

# def function(a,b):
#     return(a+b)
# sum=function(8,10)
# print(sum)

# Continue:
#  This statement returns the control to the beginning of the loop.
#  The continue statement did not accept all the remaining statements in the current loop iteration and moves the control back to the starting of the loop.
# Skips this iteration, loop keeps going.

# Example 2:

# for i in range(9):
#     if i==3:
#         continue
#     if i==5:
#         continue
#     print(i)

# Example 3:

# names=["Alice","Bob","Charlie"]

# for name in names:
#     if name=="Alice":
#         continue
#     print("Hello ", name)

# Break:
# The break statement terminated the current loop and resumes execution at the next statement.

# Example 4:
# for i in range(5):
#     if i==2:
#         break
#     print(i)


# # Pass:
# The pass statement is a do-noting.
#  This statement does nothing, code continues normally.

# Example 5:
# x=4
# if x>0:
#     pass

# # Example 6:

# print("Pass: ")
# for i in range(5):
#     if i==3:
#         pass
#     print(i)

# print("Continue: ")
# for i in range(5):
#     if i==3:
#         continue
#     print(i)


# # # Activity 1:
# # # 1) Take a word input from the user and store it in `a`.

# # 2) Use a `for` loop to iterate through each character `i` in the word `a`.

# # 3) For each character, check if it is equal to 'A':
# #    a) If `i == 'A'`, print "A is found".
# #    b) Use `break` to stop the loop immediately after finding 'A'.

# # 4) If the current character is not 'A', print "A not found".
# #    (This message prints for each character until 'A' is found or the loop ends.)

# # Activity 2:
# # 1) Use a `for` loop to iterate `x` from 0 to 9 using `range(10)`.

# # 2) For each value of `x`, check conditions in order:

# # 3) If `x % 20 == 0`, print "twist".
# #    (This is true when `x` is divisible by 20.)

# # 4) Else if `x % 15 == 0`, do nothing using `pass`.
# #    (This is true when `x` is divisible by 15, but no output is required.)

# # 5) Else if `x % 5 == 0`, print "fizz".
# #    (This is true when `x` is divisible by 5.)

# # 6) Else if `x % 3 == 0`, print "buzz".
# #    (This is true when `x` is divisible by 3.)

# # 7) Else, if none of the above conditions match, print the value of `x`.

# # Activity 3:
# # Write a program to print all the number between 1 to 10 in reverse order and skip 5

# # Activty 4:
# # Write a program to calculate the customer due amount after paying a bill of a certain amount.

#A1
# a=input("Enter a word")
# for i in a:
#     if i=="A":
#         print("A is found")
#         break
#     else:
#         print("A is not found")

# #A2
# for x in range(10):
#     if x % 20==0:
#         print("twist")
#     elif x % 15==0:
#         pass
#     elif x % 5==0:
#         print("fizz")
#     elif x % 3==0:
#         print("buzz")
#     else:
#         print(f"The value of x is,{x}")

# #A3
# for i in range(10,0,1):
#     if i==5:
#         continue
#     print(i)

# #A4
# bill_amount=int(input("Enter the amunt of bill"))
# bill_paid=int(input("Enter the amount paid by the customer"))
# due_amount=bill_amount-bill_paid
# if due_amount>0:
#     print("The customer still ows the due amount")
# else:
#     print("The customer has paid all the amount")
# Exception:
# An exception is an event theat disrupts the normal flow of the program's execution.

# Example:
# print(10/0)

# Exception error:

# x=int("abc")

# Syntax error: Wrong grammer, Rules not followed.

# Syntax Error : # Program won't start.
#  Exception : Program starts.

# syntax error:

# def greet()
#     print("")
        

# Exception handling mechanism:

# try: The try statements allows you to test a block of code for errors.
# Example for try & except: 

# try :
#     print(x)
# except:
#     print("An exception occured.")
# except: The except statement lets you handle the error.
# finally: This statement lets you execute coed, regardless of the resultof the try- and except blocks.
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally: 
#     print("The 'try except' is finished.")
# # raise: This keyword is used to raise exceptions.
# # Example:
try :
    age=int(input("Enter your age: "))
    if (age<18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("Age is not valid.")

# Important Python errors:
# Arithemetic Error: It occurs for the errors in arithemetic operations.
# Value Error: value errors occurs when a function or a built-in operation recieves ann argument of correct type but does not have a suitable value.
# ZeroDivisionError: This error is raised when its division by zero.
# IOError:This kind of error is raised when an input/output operation fails.
# syntax error: Syntax errors raised when there is a error in Pyhton syantax.
# Indentation Error: This error occurs when indentation is not propetly defined.
# NameError: A NameError is raised when a name is referred to in code that never exists in the local or global namespce.

# Activity 1:
# 1) Start a `try` block to run code that may cause exceptions.

# 2) Take two numbers from the user in a single input, separated by a comma:
#    a) Use `eval(input(...))` to read and convert the input.
#    b) Store the two values in `num1` and `num2`.

# 3) Perform division:
#    a) Compute `result = num1 / num2`.
#    b) Print the result.

# 4) Handle possible errors using multiple `except` blocks:

# 5) If a `ZeroDivisionError` occurs (when `num2` is 0),
#    print "Division by zero is error !!".

# 6) If a `SyntaxError` occurs (for example, the comma is missing or format is incorrect),
#    print a message explaining the correct input format: "1, 2".

# 7) If any other error occurs, use a general `except` block
#    and print "Wrong input".

# 8) If no exception occurs in the `try` block, run the `else` block
#    and print "No exceptions".

# 9) Run the `finally` block no matter what happens (error or no error),
#    and print "This will execute no matter what".

# Activity 2:

# 1) Create a boolean variable `valid = False`.
#    (This will be used to keep asking for input until a valid number is entered.)

# 2) Start a `while not valid` loop so the program repeats until `valid` becomes True.

# 3) Inside the loop, use a `try` block to handle invalid (non-integer) input safely.

# 4) Ask the user to enter a number and convert it to an integer:
#    a) Store the input in `n` using `n = int(input(...))`.

# 5) Use another `while` loop to check if the number is even:
#    a) Repeat while `n % 2 == 0` (meaning `n` is divisible by 2).
#    b) Print "bye" inside the loop.
#    (This loop will keep running as long as `n` stays even.)

# 6) After the inner loop ends, set `valid = True`
#    so the outer loop stops repeating.

# 7) If the user enters something that is not a number,
#    a `ValueError` occurs and the `except` block runs:
#    a) Print "Invalid"
#    b) The outer loop continues and asks again.

# Activity 3:
# Write a program to understand how the value error exception works?

#A1
try:
  num1,num2=eval(input("Enter two numbers separated by comma"))
  result=num1/num2
  print(f"The result is{result}")
except ZeroDivisionError:
    print("Division by zero is an error")
except SyntaxError:
  print("The format is incorrect")
except Exception:
  print("Wrong Input")
else:
  print("No exception")
finally:
  print("This will execute no matter what")

#A2
valid=False
while not valid:
  try:
    n=int(input("Enetr a number"))
    while n%2==0: print("bye")
   
    valid=True
  except ValueError:
   print("Invalid")

#A3
Grade=int(input("Enter your grade: "))
try:
  if (Grade<6):
        raise ValueError
  else:
        print("the grade is valid")
except ValueError:
    print("grade is not valid.")



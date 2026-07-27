# Functions: It is a block of codes of related statement that perform a specific task. If we need to control our block of code we use functions. It helps us keep our code clean and organized by dividing it into smaller chunks.
# Types of functions:
# 1. Built-in Functions: These functions are pre-defined in the python library.
# 2. User-Defined Functions:These functions that the user defines to perform specific tasks.

# Arguments: Information that are passed in functions.
# Types of arguments:
# 1. Default Arguments: These are those type of arguments whose values are default or pre-defined.
# 2. Positional Arguments: These are those type of arguments who are supposed to be passed in an order defined in the function, i.e. the first positioned argument should always be listed at the first position when function is called.

# Docstring: Its called python document string.It will help us to connect documentation with our python modules, classes or functions.
# Types :
# 1. Declaring DocString: This docstring is displayed using triple single quote '''docstring''' just below function, method, class.
# 2. Accessing DocString: This docstring can be accessed using the __doc__ method of using the function or object.
# Recursion: Funciton calling itself is called recursive function



# def my_name():
#     name="None"
#     print(name)


# def greeting():
#     greetings="Hello World"
#     print(greetings)



# for i in range(1,4):
#     my_name()
#     greeting()


# def sum(a,b): #a,b are called arguments.
#     print(a+b)

# sum(9,8) #9,8 are called parameters.
   

# def my_name(name,message="Hi"):
#     print( f"{message} {name}")

# my_name("Chintu")
# print(name)

# def sub(x,y,message):
#    print(x-y,message)

# sub(8,10,"Second time")

# def function():
#     """Demonstrates triple double quotes docstrings and does nothing else."""
#     return None

# print("Using _doc_: ",function.__doc__)

# # Functions Activity: 
# Activity 1: Write a program to create a function name well wishes that will give output hello, how are you!.

# Activity 2: Write a program to display weather in autumn & spring

# Activity 3: 
# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).

# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).

# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).

# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).

# 5) Display a menu to the user showing the available operations:
#    a) Add
#    b) Subtract
#    c) Multiply
#    d) Divide

# 6) Take the user's choice as input and store it in `choice`.

# 7) Take two integer inputs from the user:
#    a) Store the first number in `num_1`
#    b) Store the second number in `num_2`

# 8) Use conditional statements to perform the chosen operation:
#    a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
#    b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
#    c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
#    d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.






# Arguments activity:
# Activity 1: Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.

# Activity 2:Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3

# Activity 3: Write a program to find the factorial using recursive function


#A1
# def well_wishes():
#     print("Hello,how are you!")

# well_wishes()

# #A2
# def display_weather():
#     print("In autumn the weather is cool")
#     print("In spring the season is breezy")
    
# display_weather()

# #A3
def add(P,Q):
   return(P+Q)

def subtract(P,Q):
    return(P-Q)

def multiply(P,Q):
    return(P*Q)

def divide(P,Q):
    return(P/Q)

print("Select operation")
print("(a)Add")
print("(b)Subtract")
print("(c)Multiply")
print("(d)Divide")
choice=input("Enter your choice - ")
num_1=int(input("Enter first number - "))
num_2=int(input("Enter second number - "))

if choice=='a':
    print("Result is",add(num_1,num_2))
elif choice=='b':
    print("result is",subtract(num_1,num_2))
elif choice=='c':
    print("The result is",multiply(num_1,num_2))
elif  choice=='d':
    print("The result is",divide(num_1,num_2))
else:
    print("invalid input")
#A4
# def cube(number):
#     return=number*3
# def by_three(number):
#     if number%3==0:
#         return cube(number)
#     else: 
#         print("False")

#     print(by_three(6))
#     print(by_three(7))




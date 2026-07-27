import random 
import math
# Random Module and Math Module
# Random Module: In python is an built-in module which is used to generate random numbers.
# Functions of random module:
# 1. RandInt: The random.randint() method gives random integer between the specified range.
# print("This is the random number between 0 to 10: ", random.randint(0,10))
# 2. Random: This function generates a random float number between 0.0 to 1.0
# print("Random Number between 0.0 to 1.0 is: ",random.random())
# Choice: The random.choice() method returns a randomaly selected element from a non-empty sequence.
# print("This is the random selected element: ", random.choice("kashvee"))
# Seed: This function is used to apply to the particular random number with seed argument. It returns the mapper value.

# random.seed(2)
# if we use the same number (10) it will prodcuce teh same sequence every time.

# print(random.randint(1,100))
# print(random.randint(1,50))

# def hello(word,hi="Welcome"):
#     print(hi,word)

# hello("Duniya")

# def add(a,b):
#     return a+b
# result = add(3,4)
# print(result)

# Math Module:  It is built-in module in python that you can use for mathematical tasks.

# functions for math module:
# 1. ceil() : it will return the smallest integer greater than euqal to 0. c= 1.47: 2
# 2. Copysign() : Returns x with sign y.
# 3. factor(): Returns the factors of x.
# 4. floor() : it returns largest integer which less than or equal to x. c=1.47 : 1
# 5. isnan=() : Return True if the x is NaN.
# 6. exp(x) : return e**x
# 7. degree() : Converts angle x from from radians to degrees.

# Data Stuctures in Python: Data structures help you in storing a collection of data, manage them and perform different operations on them.
# We have 4 Data Structures:
# 1. List
# 2. Tuple
# 3. Dictionary
# 4. Set

# Lists: A list is the most-reliable data type available, it is commas-seperated between the values between the square brackets.
list1=[1,3,4,5,8,7] #length=
# list 1=[0,1,2,3,4,5] #positive indexing
# list 1=[-6,-5,-4,-3,-2,-1] # negative indexing
len(list1)                     

# print(list1[3]) #5

# Operations/Methods on a list:
# Size of list: Use len(), to find the number of items present in the list.
# Accessing an item from the list : slicing: We can access a range of items from the list. and indexing: We can access an item using an index number or its position.
# Iterating a list : The objects in the list can be iterated over one by one by using a for loop.
# Example:
# my_list=[5,8,"Tom",-73.5,"Emma"]

# for i in my_list:
#    print(i)
# Concatenation of two lists: The concatenation of two lists means merging of two lists. There are two ways to do it:
# 1. using '+' operator
# 2. using extend() method. This method appends the new list items at the end of the calling list.

# Example :

# my_list1=[1,2,3]
# my_list2=[4,5,6]

# # Using '+' operator: 
# my_list3=my_list1+my_list2
# print("Using '+' Operator: ",my_list3)
# # Output: [1,2,3,4,5,6]

# # Using extend() method

# my_list1.extend(my_list2)
# print("Using extend() method: ",my_list1)

# Output: [1,2,3,4,5,6]

# Nested Lists: The list can contain another list (sub-list), which in turn contains another list, and so on.
# Example: 

nested_list=[[2,4,6,8,10],
             [1,3,5,7,9]] #2-D list or matrix
print("Accessing the third element of the second list ",nested_list[1][2])

for i in nested_list:
    print("list", i, "elements")
    for j in i:
        print(j)






# Activity 1: # 1) Import the `random` module to generate random numbers.

# 2) Create a variable `playing = True` to control the game loop.

# 3) Generate a random number between 0 and 9 using `random.randint(0, 9)`
#    and convert it to a string, then store it in `number`.
#    (This is the secret number the user must guess.)

# 4) Print instructions explaining the guessing game.

# 5) Start a `while` loop that runs as long as `playing` is True:
#    a) Take a guess from the user and store it in `guess`.

# 6) Check if the user's guess matches the secret number:
#    a) If `number == guess`:
#       i) Print a winning message.
#       ii) Display the secret number.
#       iii) Stop the loop using `break` (game ends).

# 7) Otherwise (if the guess is incorrect):
#    a) Print a message telling the user to try again.
#    b) The loop continues and asks for another guess.


# Activity 2: 
# 1) Import the `random` module to let the computer make a random choice.

# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.

# 3) Take the user's choice as input and store it in `user_action`.
#    (Expected inputs: "rock", "paper", or "scissors".)

# 4) Create a list `possible_actions` containing the three valid moves.

# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move
#    and store it in `computer_action`.

# 6) Display both choices (user and computer) using an f-string.

# 7) Compare `user_action` and `computer_action` to decide the result:
#    a) If both are the same, print that it’s a tie.
#    b) Else if the user chose "rock":
#       i) If computer chose "scissors", user wins.
#       ii) Otherwise, user loses (computer chose "paper").
#    c) Else if the user chose "paper":
#       i) If computer chose "rock", user wins.
#       ii) Otherwise, user loses (computer chose "scissors").
#    d) Else if the user chose "scissors":
#       i) If computer chose "paper", user wins.
#       ii) Otherwise, user loses (computer chose "rock").

# 8) After showing the result, ask the user if they want to play again
#    and store the input in `play_again`.

# 9) If `play_again` is not "y", stop the game using `break`.
#    Otherwise, the loop continues and a new round starts.

#A1
# import random
# playing=True
# number=str(random.randint(0,9))
# print("Welcome to the guessing game!Try to guess the number between 0 to 9")
# while playing:
#   guess=int(input("Enter your guess - "))
#   if number==guess:
#     print("Yess!,That is a perfect guess")
#     print(f"The secret numer is",{number})
#     break
#   else:
#     print("Sorry.try again")

# #A2
# import random
# while True:
#     user_action=input("Enter your choice (rock,scissors,paper) - ")
#     possible_action=["rock","scissors","paper"]
#     computer_action=random.choice(possible_action)
#     print(f"you chose{user_action} and computer chose{computer_action}")
#     if computer_action==user_action:
#        print("Its a tie!")
#     elif user_action=="rock":
#        if computer_action=="scissors":
#           print("rock smashes scissors,you win!")
#        else:
#           print("Paper covers rock,you lose!")
#     elif user_action=="paper":
#        if computer_action=="rock":
#           print("Paper covers rock,you win!")
#        else:
#           print("Scissors cuts paper,you lose!")
#     elif user_action=="scissors":
#        if computer_action=="paper":
#           print("Scissors cuts paper,you win!")
#        else:
#           print("rock smashes scissors,you lose!")
#           play_again=input("Do you wanna pplay again? (y/n) - ")
#           if play_again!="y":
#              break


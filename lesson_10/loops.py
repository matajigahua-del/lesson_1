# Loops
# Types:
# 1. For Loops: It is used to iterate over a sequence like string, in for loop we can iterate over each item that is present in the sequence and perform same set of operation over them.
#  Example 1:
# n = "hello"
# for i in n:
#     print(i)

#     # Example 2:
# for i in range(10): # range(10)= Start=0, Stop=10, Step=1:
#     print(i)

# i=0 #h
# i=1 #e
# i=2 #l

# 2. While Loops : 
# 3. Nested Loops:


# Activity 1:
# 1) Ask the user to enter a number and store it in `n`.

# 2) Set `sum` to 0.
#    (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.

# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)


# Activity 2:

# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.
#    (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:
#    - Add the character `i` in front of `string2`
#    - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).

# Activity 3:

# 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.

# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).



# def function1():
#     sum=0
#     sum1=0
#     product=1
#     product1=1
#     count=0
#     count1=0

#     num1=int(input("Enter number 1: "))
#     num2=int(input("Enter number 2: "))

#     for i in range(num1):
#         sum+=i #sum=sum+i , new value 1= sum of all the numbers from 0 to num1.
#         count+=1
#         product*=i+1
        
#     for i in range(num2):
#         sum1+=i # reassigns the value of sum, new value 2= value of new value 1, sum of new value 1 and all the numbers from 0 to num2.
#         count1+=1
#         product1*=i+1
       

#     print(f"This is the sum of all the numbers from 0 to {num1}: {sum}") #f: formatted string literal, used to print a variable's value.
#     print(f"This is the sum of all the numbers from 0 to {num2}: {sum1}")
#     print(f"This is the product of all the numbers from 0 to {num1}: {product}")
#     print(f"This is the product of all the numbers from 0 to {num2}: {product1}")
#     print(f"This is the difference of {sum} and {sum1}: ", sum1-sum)
#     print(f"This is the average of numbers ranging from 0 to {num1}: ", sum/count)
#     print(f"This is the average of numbers ranging from 0 to {num2}: ", sum1/count1) 

# function1()

    #A1
# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(f"The sum of numbers from 1 to n is: {sum}")

str="python"
bag=""
for i in str:
    bag+=i
print(bag)
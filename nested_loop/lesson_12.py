# Nested Loops :
# 1. A loop inside another loop is called nested loop.
# 2. The first loop is called outer loop and the other ones are called inner loop.
# 3. The outer loop can contain multiple inner loops, no limitations.
# 4. The outer loop controls how many interations will the inner loop perform.
# 5. For each repetition of the outer loop, the inner loop restart and completes its execution.
# 6. Nested loops are mainly used for working with multi-dimensional data structures, such as 2D arrays.

# Syntax for while loop inside while loop:

# while (condition):
#     while(condition1):
#         statements
#     statements

# Example for while inside while:

# row=1 # initialise row is less than or equal to 5
# while row<=5: # iterating loop till row is less than or equal to 5
#     col=1 # intialising column such that its less than or equal to 10
#     while col<=10: # iterating loop till column is less than or equal to 10
#         print(col, end=" ")
#         col=col+1 #increment in columns
#     print() # print() with no arguments prints nothing but a newline character.It moves the cursor to the next line.
#     row=row+1 # increment in rows

# Syntax for loop inside for loop:

# Outer for loop
#  for element in sequence:
    # Inner for loop
#     for element1 in sequence1:
#         body of inner for loop
#     body of outer for loop


# Example for inside for:

for row in range(1,5): #outer loop iterates from 1 to 4 
    for col in range(1,11): #inner loop iterates fro 1 to 10
        print(col, end=" ") 
    print()

# Output
# 12345678910
# 12345678910
# 12345678910
# 12345678910


# Activity 1:
# 1) Ask the user to enter a word and store it in `string`.

# 2) Ask the user to enter a single character and store it in `char`.

# 3) Set `i` to 0.
#    (This will be used as the index to move through the string.)

# 4) Set `count` to 0.
#    (This will store how many times `char` appears.)

# 5) While `i` is less than the length of `string`:
#    a) Check if the character at position `i` in `string` is equal to `char`.
#    b) If yes, increase `count` by 1.
#    c) Increase `i` by 1 to move to the next character.

# 6) After the loop, print how many times `char` occurred in `string` using `count`.


# Activity 2:
# 1) Take two integer inputs from the user and store them in `lower` and `upper`.
#    (These represent the starting and ending range.)

# 2) Print a message showing the range: from `lower` to `upper`.

# 3) Use a loop to check every number `num` from `lower` to `upper` (inclusive).

# 4) For each `num`, first check if it is greater than 1.
#    (Because prime numbers are always greater than 1.)

# 5) If `num` is greater than 1, test if it is prime:
#    a) Try dividing `num` by every number `i` from 2 to `num - 1`.
#    b) If `num` is divisible by any `i` (remainder is 0), it is NOT prime → stop checking (break).

# 6) If the loop finishes without finding any divisor (no break happened),
#    then `num` is prime → print `num`.

# Activity 3:

# 1) Take an integer input from the user and store it in `num`.
#    Also copy the same value into `t` for digit counting.

# 2) Initialize `numLen = 0` to count the number of digits.

# 3) Count the digits using a loop:
#    a) Repeat while `t > 0`
#    b) Increase `numLen` by 1 each time
#    c) Remove the last digit of `t` using `t = int(t/10)`

# 4) Check if the number has at least 4 digits:
#    If `numLen >= 4`, continue to find the middle digits.
#    Otherwise, print: "It's not a 4 or more than 4-digit number!"

# 5) If the number has 4 or more digits:
#    a) Set `numLen = int(numLen/2)` to locate the middle positions
#    b) Initialize `chk = 0` to track the digit index while extracting digits

# 6) Extract digits from right to left:
#    a) Repeat while `num > 0`
#    b) Get the last digit using `rem = num % 10`
#    c) If `chk == numLen`, store this digit as `midOne`
#    d) Else if `chk == (numLen - 1)`, store this digit as `midTwo`
#    e) Remove the last digit using `num = int(num/10)`
#    f) Increase `chk` by 1

# 7) Multiply the two middle digits:
#    `prod = midOne * midTwo`

# 8) Print the product in the required format:
#    "Product of Mid digits (midOne * midTwo) = prod"
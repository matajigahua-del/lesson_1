# While loop:
# 1. The while loop executes a block of code while a particular condition is True, and will stop execution when condition becomes False.
# 2. While loop works when the number of repetition is not known.
# 3. While loop is used in scenarios when condition can never be False, leading to infinite loop.
# Infinite Loop: In it the program enters the loop & repeatedly reapeats the same code block, and the loop never ends.
# Syntax: 
# while (condition):
    # Block of code or statement.
# Example 1:

# i = 1
# while i < 6: #i=1 (True), i=2 (True), i=3 (True), i=4 (True), i=5 (True), i=6 (False) 
#     print(i) #print 1 2 3 4 5
#     i += 1   #i=6

# Example 2:
# i=1
# while(True):
#     print(i)
#     i+=1

#A1
#Write a program to find the sum of natural numbers and ask the user to enter the number.

num=int(input("Enter a number"))
i=1
sum=0 #>8 1+2+3+4=10 10<8 True 1+2+3+4
sum1=0
while i<num:  #i=1 1<2

    sum1=sum
    sum+=i #1

    if(sum>8): #1<8
        print("Last value of sum ",sum1)    
        break

    i+=1
# print("sum ",sum)  #10





# Activity 2: Infinite loop
# 1) Set `i` to 0.

# 2) Start a loop that keeps running as long as `i` is less than or equal to 0.

# 3) Inside the loop, print: "I WILL RUN FOREVER"

# 4) Notice: `i` is never changed inside the loop.
#    That means `i` stays 0 forever, so the condition (i <= 0) stays true forever.
#    So the loop never stops (infinite loop).


#Armstrong number are those numbers that is equal to hte sum of its own digits, each raised by the power of the number of digits.

#153 digits=3 1**3+5**3+3**3=153
# 370 digits=3 3**3+7**3+0**3=370

# Activity 3: Armstrong number
# 1) Ask the user to enter a number and store it in `num`.

# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
#    (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
#    a) Find the last digit of `temp` and store it in `digit`.
#    b) Add (digit × digit × digit) to `sum`.
#    c) Remove the last digit from `temp` so you can move to the next digit.

# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.
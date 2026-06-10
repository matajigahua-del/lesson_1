# Precedence : The precedence/priority of an operator specifies how it binds two expressions together.
# PEMDAS: Parentheses, Exponential, Multiplication, Division, Addition.
# Expression & Statement:
# Expression : Produces a value. Example: 5+3, x*2
# Statement: Performs an action. Example: x=10, if x>0, x=5+3
# Example for PEMDAS:
# 2**(3+1)=16
# (1+2)**(5-2)=27


 #1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:

# - The code checks if `name` is "Alex"

# OR (if `name` is "John" AND `age` is 2 or more).

# - If the condition is true, print the welcome message.

# - Otherwise, print the goodbye message.

#A1
v=8
w=5
x=10
y=2
z=(v+w)*x/y
print("The value of z is",z)
name="Alex"
age=23
if name=="Alex" or (name=="John" and age>=2):
    print("Welcome!")
else:
    print("Goodbye!")

     #1) Ask the user to enter the numerator and store it in `numn`.

# 2) Ask the user to enter the denominator and store it in `numd`.

# 3) Check if `numn` is divisible by `numd`:

# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.

#A2
numn=int(input("Enter a number"))
numd=int(input("enter a number"))
if numn%numd==0:
    print(numn,"is divisible by",numd)
else:
    print(numn,"is not divisible by",numd)

     #1) Store the given values:

# `mean1` (imaginary mean), `wrong_number`, `correct_number`, and `total_number`.
# 2) Calculate the total sum using the wrong mean:

# - Multiply `mean1` by `total_number`

# - Store it in `sum`

# - Print the sum.

# 3) Fix the sum to get the correct total:

# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`

# - Print the corrected sum.

# 4) Find the correct mean:

# - Divide `num2` by `total_number`

# - Store it in `mean2`

# - Print `mean2`.

 #1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.

# 2) Calculate the average of `a`, `b`, and `c`:

# - Add them and divide by 3

# - Store the result in `avg`

# - Print `avg`

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:

# - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.

# - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.

# - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.

# - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.

# - Else if `avg` is greater than only `a`, print that it is just higher than `a`.

# - Else if `avg` is greater than only `b`, print that it is just higher than `b`.

# - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".

#A3
mean_1=10
wrong_number=5
correct_number=8
total_number=5
sum=mean_1*total_number
print("The sum is:",sum)
num2=sum-wrong_number+correct_number
print("The corrected sum is",num2)
mean_2=num2/total_number
print("The corrected mean is:",mean_2)

#A4
a=int(input("Enter a  number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
avg=(a+b+c)/3
print("The average is:",avg)
if avg>a and avg>b and avg>c:
    print("The average is higher than a,b and c:")
elif avg>a and avg>b:
    print("The average is higher than a and b")
elif avg>b and avg>c:
    print("The average is higher than b and c")
elif avg>c and avg>a:
    print("The average is higher than c and a ")
elif avg>a:
    print("It is higher than a")
elif avg>b:
    print("It is higher than b")
elif avg>c:
    print("It is higher than c")
else:
    print("Invalid input")

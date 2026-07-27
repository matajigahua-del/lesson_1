#A1
# 1) Store values in `a`, `b`, and `c`.

# 2) Check an AND condition using `a and b and c`:

# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.

# 4) Check an OR condition: `a > 0 or b > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

#A2
 #1) Store values in `a`, `b`, and `c`.

# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).

# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).

# 4) Store two strings in `a` and `b`.

# 5) If `a` is not equal to `b`, print a message saying they are different.

# 6) Store new numeric values in `a` and `b`.

# 7) Check this condition: (a equals 1) is not the same as (b equals 5).

# - If exactly one of these comparisons is True, the condition becomes True.

# - If the condition is True, print "Hello".

# 8) Take an integer input from the user and store it in `a`.

# 9) Check if `a` is not divisible by 2 (remainder is not 0).

# - If true, print that `a` is not an even number (it is odd).

#A3
 #1) Ask the user to enter their height in centimeters and store it in `height`.

# 2) Ask the user to enter their weight in kilograms and store it in `weight`.

# 3) Calculate BMI using the formula:

# BMI = weight ÷ (height in meters)²

# (Convert height from cm to meters by dividing by 100.)

# Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:

# - If BMI is 18.4 or less → print "underweight"

# - Else if BMI is 24.9 or less → print "healthy"

# - Else if BMI is 29.9 or less → print "over weight"

# - Else if BMI is 34.9 or less → print "severely over weight"

# - Else if BMI is 39.9 or less → print "obese"

# - Else → print "severely obese"

#A1
a = True
b = True
c = True
if a and b and c:
    print("All true")
else:
    print("at least one is false")
    a=89
    b=65
    c=-45
    if a>0 or b>0:
        print("either is greater than 0")
    else:
        print("no number is greater than 0")
    if b>0 or c>0:
        print("either of them is greater than 0")
    else:
        print("no number is greater than 0")

#A2
a=67
b=89
if a!=b:
    print("true")
else:
    print("False")
    a="Hello"
    b="World"
    if a!=b:
        print("They are different")
        a=2
        b=5
        if (a==1) != (b==5):
            print("Hello")
            a=int(input("Enter an integer:"))
            if a%2!=0:
                print(a,"is not an even number, it is odd.")

#A3
height=int(input("Enter your height in cm:"))
weight=int(input("Enter your weight in kg:"))
BMI=weight/((height/100)**2)
print("Your BMI is:", BMI)
if BMI<=18.4:
    print("underweight")
elif BMI<=24.9:
    print("healthy")
elif BMI<=29.9:
    print("over weight")
elif BMI<=34.9:
    print("severely over weight")
elif BMI<=39.9:
    print("obese")
else:
    print("severely obese")


    

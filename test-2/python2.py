# Build a calculator that uses a separate function for each operation. The user picks an operation and enters two numbers. Your program handles invalid input and division by zero without crashing.

def add(P,Q):
    return(P+Q)
def subtract(P,Q):
    return(P-Q)
def multiply(P,Q):
    return(P*Q)
def divide(P,Q):
    return(P/Q)
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))

print("Select an operation")
print("(a)add")
print("(b)subtract")
print("(c)multiply")
print("(d)divide")
choice=input("Enter your operation")

try:
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))

except ValueError:
   print("Invalid input")

if num2==0:

    raise ZeroDivisionError("Error!Any number cannot be divided by zero")    
else:
   print("Everything is correct")
   



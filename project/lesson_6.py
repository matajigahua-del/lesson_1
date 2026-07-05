try:
    age=int(input("Enter your age:"))
    if age<0:
        raise ValueError("Age cannot be negative")
    if age%2==0:
        print("Your age is even")
    else:
        print("Your age is odd")
except ValueError :
    print(f"Error: Invalid input. Please enter a valid age.")
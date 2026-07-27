print("password challenge")
import random
import string
lenght=int(input("Enter the length of the password - "))
characters=string.ascii_letters+string.digits+string.punctuation
password="" 
for i in range(lenght):
    password+=random.choice(characters)
print("The generated password is:",password)
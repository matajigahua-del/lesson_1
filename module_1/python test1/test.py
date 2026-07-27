# Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt.

# 💡 Hint: Store your secret number in a variable — for example: secret = 27



# If you already know the random module, feel free to use it! This test checks your logic (conditions, loops, input/output).


# What you need to use
# ------------------------------------------------------------------------
# 1. int(input()) → to read the player's guess
# 2. while loop → stops after 5 attempts or when player wins
# 3. if/elif/else → hint system —

# 🧊 ice cold, 🥶 cold, 🌡️ warm, or 🔥 hot 
# 4. for loop → shows 
# emaining ❤️ hearts

# after each wrong guess
# 5. win/loss message → reveals the secret number if attempts run out

secret=49
attempt_1=int(input("Enter your first guess"))
attempt_2=int(input("Enter your second guess"))
attempt_3=int(input("Enter your third guess"))
attempt_4=int(input("Enter your fourth guess"))
attempt_5=int(input("Enter your fifth guess"))
if attempt_1<=10 or attempt_1<=20:
    print(" ice cold")
elif attempt_1>=45:
    print("hot")
elif attempt_2<=30:
    print("cold")
elif attempt_2==49:
  print("wins")
elif attempt_3>=40:
   print("hot")
elif attempt_4<=40:
   print("warm")
elif attempt_5==40:
   print("warm")
else:
   print("invalid input")

while attempt_5<=49:
   print("The secret number is",secret)
   break

# ---------------------------------------------
# ------------------------------------------------------------------------
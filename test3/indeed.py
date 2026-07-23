# # Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade. 

# # What you need to use
# # ------------------------------------------------------------------------
# # 1. dictionary → store at least 5 student name-score pairs
# # 2. for loop → to calculate the class average
# # 3. max() min() → to find the top and bottom scorer
# # 4. .get() → to look up a student by name
# # 5. input() → to let the user search for a student
# # ------------------------------------------------------------------------

# # What you'll be marked on
# # ------------------------------------------------------------------------
# # 1. Dictionary created with at least 5 student name-score pairs → 5 marks
# # 2. A loop correctly calculates and prints the class average → 10 marks
# # 3. Highest and lowest scores and students identified → 10 marks
# # 4. .get() used to look up student — friendly message if missing → 10 marks
# # 5. Program runs without any errors → 5 marks
# # ===================================================================

gradebook={"Alice":67,
           "bob":88,
           "nicey":89,
           "riya":99,
           "rohan":100 
           }
total_score=gradebook of score

for  total_score in gradebook:
    total_score+=gardebook of score
    print(total_score)
   
    
top_score=max(gradebook)
bottom_score=min(gradebook)
for name,total_score in gradebook:
    if total_score==top_score:
      print(f"The top scorer is",{top_score})
    else:
      print(f"The bottom scorer is",{bottom_score})
      search_name=input("Enter the name of the student")
      result=gradebook.get(search_name)
      print





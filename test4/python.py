# Build a simple library system using a class. Each book is an object. Your system lets users borrow and return books and tracks whether each book is currently available. 

# What you need to use
# ------------------------------------------------------------------------
# 1. Book class → __init__ sets title, author, and is_borrowed = False
# 2. borrow() → sets is_borrowed to True and prints a confirmation
# 3. return_book() → sets is_borrowed to False and prints a confirmation
# 4. 3 Book objects → demonstrate both borrow() and return_book()
# 5. self → used to access and update attributes inside methods
#A1
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print("Okaii you have the access to the book")
        else:
            print(f"sorry {self.title} book is already borrowed")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"Thankssss for returning the {self.title}")
        else:
            print(f"{self.title}book is not returned")
book_1=book("Diary of a wimpy kid","Jeff Kinny")
book_2=book("Atomic Habits","James Clear")
book_3=book("The Locked door","Frieda Mcfadden")
print("Testing book_1")
book_1.borrow()
book_1.borrow()
print("Testing book_2")
book_2.return_book()
book_2.borrow()
book_2.return_book()

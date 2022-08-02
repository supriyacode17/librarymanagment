class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):   
        print("Books Present in this library are:") 
        for book in self.books:
            print("\t " + book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued{bookName}. Please keep it safe and return on time")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry , This book is issued to someone else, please wait until the book is returned")    
            return False


    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Have a great day ahead!")

class Student:

    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of book you want to return")
        return self.book
    
if __name__ == "__main__":
    centrallibrary = Library(["Python","Javascript","Java","PHP","C++","DBMS","PLC","HTML","CSS"])
    student = Student()
   # centrallibrary.displayAvailableBooks()
    while(True):
        welcomeMsg=""""====Welcome to Centeral Library====
        Please choose an option:
        1.  List all the books
        2.  Request a book
        3.  Return a book
        4.  Exit the library
        """
        print(welcomeMsg)
        a = int(input("Enter a choice:"))
        if a == 1:
            centrallibrary.displayAvailableBooks()
        elif a == 2:
            centrallibrary.borrowBook(student.requestBook())
        elif a == 3:
            centrallibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central libarary. Have a great day") 
            exit()
        else:
            print("Invalid choice!")    

       





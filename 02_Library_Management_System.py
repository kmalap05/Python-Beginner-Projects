class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def display_books(self):
        print()
        count = 1
        while True:
            for bookNames in self.books:
                print(" " + str(count) + ". " + bookNames)
                count += 1
            break
        print()

    def borrow_book(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def return_book(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:

    def borrow_book(self):
        self.bookName = input("Book Name To Borrow: ")
        return self.bookName

    def return_book(self):
        self.bookName = input("Book Name To Return: ")
        return self.bookName


if __name__ == '__main__':

    library = Library(['Java Programming', 'C Programming',
                      'Data Structures And Analysis', 'Operating System', 'CyberSecurity'])
    student = Student()

    while True:
        print('''***** WELCOME TO KEDAR LIBRARY *****
        1. List Of Books Available
        2. Request A Book
        3. Return A Book
        4. Exit
************************************''')

        choice = int(input("Enter Your Choice: "))
        print("************************************")

        if choice == 1:
            library.display_books()
        elif choice == 2:
            library.borrow_book(student.borrow_book())
        elif choice == 3:
            library.return_book(student.return_book())
        elif choice == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

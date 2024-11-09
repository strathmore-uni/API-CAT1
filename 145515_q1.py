class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  
    
    def borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow(self, book):
        if book.borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is unavailable.")
    
    def returned(self, book):
        if book in self.borrowed_books:
            book.returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")
    
    def list_of_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

if __name__ == "__main__":

    book1 = Book("Born a Crime", "Trevor Noah")
    book2 = Book("Animal Farm", "George Orwell")
    book3 = Book("Africa Kills Her Sun", "Ken Saro")
    
    member = LibraryMember("Ogoro Ruth", "12345")
    
    books = [book1, book2, book3]  
    
    while True:
        print("\nLibrary System:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable books:")
            available_books = [book for book in books if not book.is_borrowed]
            if available_books:
                for i, book in enumerate(available_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                
                book_choice = input("Enter the number of the book to borrow: ")
                try:
                    book_index = int(book_choice) - 1
                    if 0 <= book_index < len(available_books):
                        member.borrow(available_books[book_index])
                    else:
                        print("Invalid choice. Please select a valid book number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No books are available for borrowing.")

        elif choice == "2":
            if member.borrowed_books:
                print("\nYour borrowed books:")
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                
                return_choice = input("Enter the number of the book to return: ")
                try:
                    return_index = int(return_choice) - 1
                    if 0 <= return_index < len(member.borrowed_books):
                        member.returned(member.borrowed_books[return_index])
                    else:
                        print("Invalid choice. Please select a valid book number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("You have no borrowed books to return.")

        elif choice == "3":
            member.list_of_borrowed_books()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


        

        
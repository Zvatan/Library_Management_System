def splitlines(self):
    return self.strip().split(',')
            
class Library:
    def __init__(self, file_name="books.txt"):
        try:
            self.file = open(file_name, "a+")
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Creating a new file.")
            self.file = open(file_name, "a+")

    def __del__(self):
        if self.file:
            self.file.close()
            print(f"File '{self.file.name}' closed.")
    
    def list_books(self):
        self.file.seek(0)
        lines = self.file.readlines()
        if not lines:
            print("No books found.")
        else:
            print("List of books:")
            for line in lines:
                book_info = splitlines(line)
                if len(book_info) >= 2:
                    book_title, book_author = book_info[:2]
                    print(f"Title: {book_title}, Author: {book_author}")
    
    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{book_title}' added successfully.")

    def remove_book(self):
        book_title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        lines = [line for line in self.file.readlines() if book_title_to_remove not in line]
        
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(lines)
        print(f"Book '{book_title_to_remove}' removed successfully.")

# Example Usage:
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        lib.list_books()
    elif user_choice == "2":
        lib.add_book()
    elif user_choice == "3":
        lib.remove_book()
    elif user_choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

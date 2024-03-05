class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            return False
        else:
            self.is_borrowed = True
            return True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn and not b.is_borrowed), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        if book and member:
            return member.borrow(book)
        return False

    def return_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        if book and member:
            return member.return_book(book)
        return False

    def __str__(self):
        available_books = len([b for b in self.books if not b.is_borrowed])
        return f"Library with {len(self.books)} books ({available_books} available), {len(self.members)} members"

# Example usage
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
member = Member("John Doe", "M001")

library.add_book(book1)
library.add_book(book2)
library.register_member(member)

# Borrowing and Returning books
print(library.borrow_book("123456789", "M001"))  # True, borrowing successful
print(library.borrow_book("987654321", "M001"))  # True, borrowing successful

print(book1.is_borrowed)  # Should be True

print(library.return_book("123456789", "M001"))  # True, returning successful
print(book1.is_borrowed)  # Should be False

# Displaying Library Info
print(library)  # Shows total books and members

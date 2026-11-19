
class Book:
    """
    A class representing a library book.
    Stores and updates book information.
    """

    def __init__(self, title, author, ISBN, publication_year):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_year = publication_year

    def display_details(self):
        """Display the details of a book."""
        print("\n----- BOOK DETAILS -----")
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.ISBN)
        print("Publication Year:", self.publication_year)

    def update_author(self, new_author):
        """Update the author's name."""
        self.author = new_author


book1 = Book(
    "Things Fall Apart",
    "Chinua Achebe",
    "9780385474542",
    1958
)

book2 = Book(
    "The River Between",
    "Ngugi wa Thiong'o",
    "9780435905484",
    1965
)

book3 = Book(
    "Born a Crime",
    "Trevor Noah",
    "9780399588174",
    2016
)


books = [book1, book2, book3]


print("INITIAL BOOK DETAILS")

for book in books:
    book.display_details()


print("\nUPDATING THE AUTHOR OF BOOK ONE")

book1.update_author("Chinua Achebe (Updated Author)")


print("\nUPDATED BOOK DETAILS")

for book in books:
    book.display_details()

from typing import List, Dict, Optional

# Our "database" of books. It will be a list where each book is a dictionary.
library: List[Dict[str, any]] = []

# List of allowed literary genres.
valid_genres: List[str] = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

def add_book() -> None:
    """Allows adding a new book to the library."""
    print("\n--- Add New Book ---")
    title: str = input("Book title: ")
    author: str = input("Book author: ")
    # Let's make sure the quantity is an integer.
    while True:
        try:
            quantity_str: str = input("Number of available copies: ")
            quantity: int = int(quantity_str)
            if quantity >= 0:
                break
            else:
                print("The quantity must be a positive number.")
        except ValueError:
            print("Please enter an integer for the quantity.")

    # We validate the genre against our list of allowed genres.
    while True:
        genre: str = input(f"Literary genre ({', '.join(valid_genres)}): ").capitalize()
        if genre in valid_genres:
            break
        else:
            print(f"Invalid genre. Please choose from: {', '.join(valid_genres)}.")

    # We create a dictionary that represents the book.
    new_book: Dict[str, any] = {
        "title": title,
        "author": author,
        "quantity": quantity,
        "genre": genre,
        "total_copies": quantity # We save the original quantity for deletion.
    }
    library.append(new_book)
    print(f"\nBook '{title}' has been added to the library!")

def search_book() -> None:
    """Allows searching for the details of a book by its title."""
    print("\n--- Search Book ---")
    search_title: str = input("Enter the title of the book you are looking for: ")
    found: bool = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            print("\nBook details:")
            print(f"  Title: {book['title']}")
            print(f"  Author: {book['author']}")
            print(f"  Available copies: {book['quantity']}")
            print(f"  Genre: {book['genre']}")
            found = True
            break
    if not found:
        print(f"\nSorry, the book '{search_title}' is not in the library.")

def borrow_book() -> None:
    """Registers the borrowing of a book, decreasing the available quantity."""
    print("\n--- Borrow Book ---")
    borrow_title: str = input("Enter the title of the book you want to borrow: ")
    found: bool = False
    for book in library:
        if book["title"].lower() == borrow_title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print(f"\nThe book '{book['title']}' has been borrowed!")
                print(f"There are now {book['quantity']} copies available.")
            else:
                print(f"\nSorry, there are no copies available of the book '{book['title']}'.")
            found = True
            break
    if not found:
        print(f"\nSorry, the book '{borrow_title}' is not in the library.")

def return_book() -> None:
    """Registers the return of a book, increasing the available quantity."""
    print("\n--- Return Book ---")
    return_title: str = input("Enter the title of the book you are returning: ")
    found: bool = False
    for book in library:
        if book["title"].lower() == return_title.lower():
            book["quantity"] += 1
            print(f"\nThe book '{book['title']}' has been returned!")
            print(f"There are now {book['quantity']} copies available.")
            found = True
            break
    if not found:
        print(f"\nSorry, the book '{return_title}' is not in the library.")

def delete_book() -> None:
    """Allows deleting a book from the catalog if there are no borrowed copies."""
    print("\n--- Delete Book ---")
    delete_title: str = input("Enter the title of the book you want to delete: ")
    delete_index: int = -1
    for i, book in enumerate(library):
        if book["title"].lower() == delete_title.lower():
            if book["quantity"] == book["total_copies"]:
                delete_index = i
                break
            else:
                print(f"\nCannot delete '{book['title']}'. There are still borrowed copies.")
                break
    if delete_index != -1:
        deleted_book: Dict[str, any] = library.pop(delete_index)
        print(f"\nThe book '{deleted_book['title']}' has been deleted from the catalog!")
    elif delete_index == -1 and not any(book["title"].lower() == delete_title.lower() for book in library):
        print(f"\nSorry, the book '{delete_title}' is not in the library.")

def list_books_by_genre() -> None:
    """Shows all available books of a specific genre."""
    print("\n--- List Books by Genre ---")
    search_genre: str = input(f"Enter the genre you want to list ({', '.join(valid_genres)}): ").capitalize()
    if search_genre not in valid_genres:
        print(f"\nInvalid genre. Please choose from: {', '.join(valid_genres)}.")
        return

    found_books: List[str] = []
    for book in library:
        if book["genre"] == search_genre:
            found_books.append(book["title"])

    if found_books:
        print(f"\nBooks of genre '{search_genre}':")
        for title in found_books:
            print(f"- {title}")
    else:
        print(f"\nThere are no available books of the genre '{search_genre}'.")

def show_inventory_summary() -> None:
    """Indicates how many books and total copies there are in the library."""
    total_books: int = len(library)
    total_available_copies: int = sum(book["quantity"] for book in library)
    print("\n--- Inventory Summary ---")
    print(f"Total books in the library: {total_books}")
    print(f"Total available copies: {total_available_copies}")

def main() -> None:
    """Main function that runs the library management system."""
    while True:
        print("\n--- Library Management System ---")
        print("1. Add book")
        print("2. Search book by title")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Delete book")
        print("6. List books by genre")
        print("7. Show inventory summary")
        print("8. Exit")

        option: str = input("Choose an option (1-8): ")

        if option == '1':
            add_book()
        elif option == '2':
            search_book()
        elif option == '3':
            borrow_book()
        elif option == '4':
            return_book()
        elif option == '5':
            delete_book()
        elif option == '6':
            list_books_by_genre()
        elif option == '7':
            show_inventory_summary()
        elif option == '8':
            print("\nThank you for using the library management system!")
            break
        else:
            print("\nInvalid option. Please choose a number from 1 to 8.")

# --- Initialization with at least 10 books for testing ---
initial_books: List[Dict[str, any]] = [
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "quantity": 5, "genre": "Children", "total_copies": 5},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "quantity": 3, "genre": "Fiction", "total_copies": 3},
    {"title": "Cosmos", "author": "Carl Sagan", "quantity": 2, "genre": "Science", "total_copies": 2},
    {"title": "Steve Jobs", "author": "Walter Isaacson", "quantity": 4, "genre": "Biography", "total_copies": 4},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "quantity": 1, "genre": "Fiction", "total_copies": 1},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "quantity": 3, "genre": "Science", "total_copies": 3},
    {"title": "Becoming", "author": "Michelle Obama", "quantity": 2, "genre": "Biography", "total_copies": 2},
    {"title": "The Very Hungry Caterpillar", "author": "Eric Carle", "quantity": 6, "genre": "Children", "total_copies": 6},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "quantity": 4, "genre": "Non-Fiction", "total_copies": 4},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "quantity": 2, "genre": "Fiction", "total_copies": 2},
    {"title": "Foundation", "author": "Isaac Asimov", "quantity": 3, "genre": "Science", "total_copies": 3} # One extra book to have more than 10.
]

for initial_book in initial_books:
    library.append(initial_book)

print("\n11 initial books have been added to test the system!")

if __name__ == "__main__":
    main()

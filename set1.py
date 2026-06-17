# set1.py

from typing import Dict, List, Optional

# Part 1: Set operations

def create_unique_set(numbers: List[int]) -> set:
    """Return a set of unique numbers from the given list."""
    return set(numbers)


def add_elements(target_set: set, elements: List[int]) -> None:
    """Add new elements to the set."""
    target_set.update(elements)


def remove_elements(target_set: set, elements: List[int]) -> None:
    """Remove existing elements from the set if they exist."""
    for element in elements:
        target_set.discard(element)


def perform_set_operations(base_set: set, other_set: set) -> Dict[str, set]:
    """Return union, intersection, and difference of two sets."""
    return {
        "union": base_set.union(other_set),
        "intersection": base_set.intersection(other_set),
        "difference": base_set.difference(other_set),
    }


# Part 2: Library dictionary storage

BookInfo = Dict[str, object]
Library = Dict[str, BookInfo]


def add_book(library: Library, title: str, author: str, year: int, genre: str) -> None:
    """Add a new book to the library dictionary."""
    library[title] = {
        "author": author,
        "year": year,
        "genre": genre,
    }


def remove_book(library: Library, title: str) -> bool:
    """Remove an existing book by title. Returns True if removed."""
    if title in library:
        del library[title]
        return True
    return False


def search_books_by_title(library: Library, search_title: str) -> Library:
    """Search for books whose title contains the search text."""
    search_lower = search_title.lower()
    return {
        title: info
        for title, info in library.items()
        if search_lower in title.lower()
    }


def search_books_by_author(library: Library, author_name: str) -> Library:
    """Search for books by author name."""
    search_lower = author_name.lower()
    return {
        title: info
        for title, info in library.items()
        if search_lower in str(info.get("author", "")).lower()
    }


def search_books_by_genre(library: Library, genre_name: str) -> Library:
    """Search for books by genre."""
    search_lower = genre_name.lower()
    return {
        title: info
        for title, info in library.items()
        if search_lower in str(info.get("genre", "")).lower()
    }


def display_books_sorted_by_title(library: Library) -> List[BookInfo]:
    """Return a list of books sorted by title."""
    return [
        {"title": title, **info}
        for title, info in sorted(library.items(), key=lambda item: item[0].lower())
    ]


def display_books_sorted_by_author(library: Library) -> List[BookInfo]:
    """Return a list of books sorted by author."""
    return [
        {"title": title, **info}
        for title, info in sorted(library.items(), key=lambda item: item[1].get("author", "").lower())
    ]


def print_books(book_list: List[BookInfo], header: str) -> None:
    """Print a formatted list of books."""
    print(header)
    if not book_list:
        print("  (no books found)")
        return
    for book in book_list:
        print(f"  - {book['title']} by {book['author']} ({book['year']}) [{book['genre']}]")
    print()


# Sample test driver

def main():
    print("--- Set Operations Demo ---")
    raw_numbers = [5, 2, 5, 9, 2, 7, 7, 1]
    unique_numbers = create_unique_set(raw_numbers)
    print(f"Initial unique numbers: {sorted(unique_numbers)}")

    add_elements(unique_numbers, [3, 10])
    print(f"After adding [3, 10]: {sorted(unique_numbers)}")

    remove_elements(unique_numbers, [2, 99])
    print(f"After removing [2, 99]: {sorted(unique_numbers)}")

    other_set = {1, 2, 3, 8, 10}
    ops = perform_set_operations(unique_numbers, other_set)
    print(f"Union with {sorted(other_set)}: {sorted(ops['union'])}")
    print(f"Intersection with {sorted(other_set)}: {sorted(ops['intersection'])}")
    print(f"Difference with {sorted(other_set)}: {sorted(ops['difference'])}")

    print("\n--- Library Dictionary Demo ---")
    library: Library = {}

    add_book(library, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    add_book(library, "A Brief History of Time", "Stephen Hawking", 1988, "Science")
    add_book(library, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    add_book(library, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
    add_book(library, "Dune", "Frank Herbert", 1965, "Science Fiction")

    print_books(display_books_sorted_by_title(library), "Books sorted by title:")
    print_books(display_books_sorted_by_author(library), "Books sorted by author:")

    print("Searching for books with title containing 'the':")
    print_books(
        [{"title": title, **info} for title, info in search_books_by_title(library, "the").items()],
        "Search results by title:",
    )

    print("Searching for books by author 'Tolkien':")
    print_books(
        [{"title": title, **info} for title, info in search_books_by_author(library, "Tolkien").items()],
        "Search results by author:",
    )

    print("Searching for books in genre 'Science':")
    print_books(
        [{"title": title, **info} for title, info in search_books_by_genre(library, "Science").items()],
        "Search results by genre:",
    )

    removed = remove_book(library, "The Great Gatsby")
    print(f"Removed 'The Great Gatsby': {removed}")
    print_books(display_books_sorted_by_title(library), "Books after removal:")

    print("Final library contents:")
    print_books(display_books_sorted_by_title(library), "Final sorted by title:")


if __name__ == "__main__":
    main()

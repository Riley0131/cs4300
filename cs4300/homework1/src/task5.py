favorite_book = [
    ["book1", "author1", "student1"],
    ["book2", "author2", "student2"],
    ["book3", "author3", "student3"],
    ["book4", "author4", "student4"],
    ["book5", "author5", "student5"],
]

# Get the first 3 books
first_three = favorite_book[:3]

# Build dictionary
books = {book: {"author": author, "student_id": sid} for book, author, sid in first_three}


import task5

#test the dictionary
def test_books_dict():
    assert task5.books == {
        'book1': {'author': 'author1', 'student_id': 'student1'},
        'book2': {'author': 'author2', 'student_id': 'student2'},
        'book3': {'author': 'author3', 'student_id': 'student3'},
    }

#test the list
def test_books():
    assert task5.favorite_book == [
        ["book1", "author1", "student1"],
        ["book2", "author2", "student2"],
        ["book3", "author3", "student3"],
        ["book4", "author4", "student4"],
        ["book5", "author5", "student5"],
    ]
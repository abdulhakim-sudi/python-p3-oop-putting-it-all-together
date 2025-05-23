from lib.book import Book

def test_book_initialization():
    book = Book("And Then There Were None", 272, "Mystery")
    assert book.title == "And Then There Were None"
    assert book.page_count == 272
    assert book.genre == "Mystery"

def test_book_attribute_modification():
    book = Book("Old Title", 100, "Fiction")
    book.title = "New Title"
    book.page_count = 200
    book.genre = "Thriller"
    assert book.title == "New Title"
    assert book.page_count == 200
    assert book.genre == "Thriller"

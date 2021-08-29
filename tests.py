import unittest

from app import create_app
from app import db
from app.blueprints.projects.cog.apps.book_library.model import Book
from app.models.user import User

from config import TestConfig


class BookModelCase(unittest.TestCase):
    # The setUp() and tearDown() methods are special methods that the unit testing
    # framework executes before and after each test respectively
    def setUp(self) -> None:
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # test methods must start with "test_"
    def test_create_book(self) -> None:
        book1 = Book(name="Dune", author="Frank Herbert")
        book2 = Book(name="Art of War", author="Sun Tzu")
        self.assertTrue(book1.name == "Dune" and book1.author == "Frank Herbert")
        self.assertTrue(book2.name == "Art of War" and book2.author == "Sun Tzu")
        self.assertFalse(book1.name == "Art of War")

        book1.save_to_db()
        book2.save_to_db()

        self.assertTrue(len(Book.find_all()) == 2)

        book = Book.find_by_name("Dune")
        self.assertTrue(book.name == "Dune")

    def test_password_hashing(self) -> None:
        user = User(username="danny",
                    password="test",
                    email="danny@example.com")
        self.assertFalse(user.is_password_valid("1234"))
        self.assertTrue(user.is_password_valid("test"))

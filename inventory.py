# library_manager/inventory.py

import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DATA_FILE = Path("book_data.json")


class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if DATA_FILE.exists():
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                    for b in data:
                        self.books.append(Book(**b))
            else:
                self.save_data()
            logging.info("Catalog Loaded Successfully")
        except Exception as e:
            logging.error(f"Error loading data: {e}")

    def save_data(self):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
            logging.info("Catalog Saved Successfully")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()
        logging.info(f"Added Book: {title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books

# cli/main.py

from library_manager.inventory import LibraryInventory

lib = LibraryInventory()

def menu():
    while True:
        print("\n====== LIBRARY INVENTORY MANAGER ======")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        
        choice = input("\nEnter Choice (1-6): ")

        try:
            if choice == '1':
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                lib.add_book(title, author, isbn)
                print("Book Added Successfully!")

            elif choice == '2':
                isbn = input("Enter ISBN to Issue: ")
                book = lib.search_by_isbn(isbn)
                if book and book.issue():
                    lib.save_data()
                    print("Book Issued Successfully!")
                else:
                    print("Book Not Available or Incorrect ISBN")

            elif choice == '3':
                isbn = input("Enter ISBN to Return: ")
                book = lib.search_by_isbn(isbn)
                if book:
                    book.return_book()
                    lib.save_data()
                    print("Book Returned Successfully!")
                else:
                    print("Book Not Found")

            elif choice == '4':
                for b in lib.display_all():
                    print(b)

            elif choice == '5':
                keyword = input("Enter Title or ISBN: ")
                results = lib.search_by_title(keyword)
                if results:
                    for b in results:
                        print(b)
                else:
                    book = lib.search_by_isbn(keyword)
                    print(book if book else "No Match Found")

            elif choice == '6':
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid Input!")

        except Exception as e:
            print("Error occurred:", e)


if __name__ == "__main__":
    menu()

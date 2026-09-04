from datetime import date, timedelta


class Book:
    def __init__(self, sku, title, author, pages, shelf_number):
        self.sku = sku
        self.title = title
        self.author = author
        self.pages = pages
        self.shelf_number = shelf_number

        self.is_available = True
        self.borrowed_date = None
        self.return_date = None

    def take_book(self):
        if self.is_available:
            self.is_available = False
            self.borrowed_date = date.today()
            self.return_date = self.borrowed_date + timedelta(days=14)
            return True
        else:
            return False

    def return_book(self):
        if self.is_available:
            return False
        else:
            self.is_available = True
            self.borrowed_date = None
            self.return_date = None
            return True

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nShelf number: {self.shelf_number}\nBorrowed date: {self.borrowed_date}\nReturn date: {self.return_date}\n\n" 


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        self.books[book.sku] = book

    def find_book(self, sku) -> Book | None:
        return self.books.get(sku)

    def list_available_books(self) -> dict:
        list_of_titles = {}
        for book in self.books.values():
            if book.is_available:
                list_of_titles[book.sku] = book.title
        return list_of_titles




def main():
    book1 = Book(1001, "Война и Мир", "Лев Николаевич Толстой", 2500, "12B04")
    book2 = Book(1002, "Мастер и Маргарита", "Михаил Афанасьевич Булгаков", 1000, "14A05")
    book3 = Book(1003, "Преступление и наказание", "Федор Михайлович Достоевский", 800, "13A12")
    lib = Library()

    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)


    while True:
        action = input("\n1. Show list of available books.\n2. Find book.\n3. Exit\n\nEnter action: ")

        if action == "1":
            list_of_titles = lib.list_available_books()
            if not list_of_titles:
                print("\nNo books are available at this moment\n")
            else:
                print("\nList of available books in library:\n")
                for sku, title in list_of_titles.items():
                    print(f"SKU: {sku}, Title: {title}")

        elif action == "2":

            sku = int(input("\nEnter book SKU: \n"))
            book = lib.find_book(sku)
            if book == None:
                print(f"\nNo books founded by SKU '{sku}'\n")
            else:
                print(book)
                print(f"\nIf you want to take book {book.title}, enter Y, if not, enter N:\n")
                yes_or_no = input()
                if yes_or_no.lower() == "y":
                    if book.take_book():
                        print(f"\nBook {book.title} taken successfully!\n")
                elif yes_or_no.lower() == "n":
                    continue
                
        elif action == "3":
            break

        else:
            print("Unavailable action, try again.")


if __name__ == "__main__":
    main()
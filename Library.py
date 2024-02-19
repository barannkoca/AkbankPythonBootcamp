class library:
    def __init__(self):
        self.file = open("Books.txt", "a+")

    def __del__(self):
        self.file.close()

    def listBooks(self):
        self.file.seek(0)
        books = self.file.read().splitlines()

        for line in books:
            bookInfo = line.split(",")
            bookName = bookInfo[0].strip()
            author = bookInfo[1].strip()

            print(f"Book: {bookName}, Author: {author}\n")

    def addBook(self):
        newBookName = input("Enter the name of the new book: ")
        newBookAuthor = input("Enter the author of the new book: ")
        newReleaseDate = input("Enter the release date of the new book: ")
        newNumberOfPages = input("Enter the number of pages of the new book: ")

        book = newBookName + ", " + newBookAuthor + ", " + newReleaseDate + ", " + newNumberOfPages + "\n"

        self.file.write(book)

    def removeBook(self):
        deleteBook = input("Enter the name of the book that you want to delete: ")

        self.file.seek(0)
        books = self.file.read().splitlines()
        index = -1
        for line in books:
            bookInfo = line.split(",")
            if bookInfo[0] == deleteBook:
                index = books.index(line)

        if index == -1:
            print(deleteBook + " couldn't find in the library!")
        else:
            books.pop(index)
            
            self.file.seek(0)
            self.file.truncate()
            
            for line in books:
                self.file.write(line + "\n")

lib = library()
while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    choice = int(input("Please enter a number: "))
    if choice == 1:
        lib.listBooks()
    elif choice == 2:
        lib.addBook()
    elif choice == 3:
        lib.removeBook()
    else:
        print("Wrong number, please try again.")
        break

lib.__del__()

    
from Objects import Book, Library

libraries = []
books = []

#reading general info
file = open("test_cases/b_read_on.txt", "r")

numOfBooks, numOfLibrary, scanningDays = file.readline().split()

## read scores for books
booksScores = file.readline().split()

for i in range(int(numOfBooks)):
    bo = Book(i, int(booksScores.__getitem__(i)))
    books.append(bo)

## reads library general info
for i in range(int(numOfLibrary)):

    libNumBooks, signUpTime, scanningLimit = file.readline().split()
    lib = Library(i, signUpTime, libNumBooks, scanningLimit)

    booksInLib = file.readline().split()

    for j in range(int(lib.numBooks)):
        lib.addBook(books.__getitem__(int(booksInLib.__getitem__(j))))

    libraries.append(lib)
    lib.toString()